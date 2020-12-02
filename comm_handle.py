import serial.threaded
import threading
import logging

try:
    import queue
except ImportError:
    import Queue as queue

class CommException(Exception):
    pass

#
# ser = serial.Serial()
# ser.baudrate = 115200
# ser.port = 'COM3'
# ser.timeout = 1
# ser.setRTS(False)
# ser.open()
#
# ser.write(b'x#')
#
# data = []
# # while (data[len(data)] != 'END'):
# a = ser.read_until('o')
# print(a)
# ser.close()

class CommProtocol(serial.threaded.LineReader):

    TERMINATOR = b'\r\n'

    def __init__(self):
        super(CommProtocol, self).__init__()
        self.alive = True
        self.responses = queue.Queue()
        self.events = queue.Queue()
        self._event_thread = threading.Thread(target=self._run_event)
        self._event_thread.daemon = True
        self._event_thread.name = 'ser-event'
        self._event_thread.start()
        self.lock = threading.Lock()
        self.event_responses = queue.Queue()
        self._awaiting_response_for = None

    def stop(self):
        """
        Stop the event processing thread, abort pending commands, if any.
        """
        self.alive = False
        self.events.put(None)
        self.responses.put('<exit>')

    def _run_event(self):
        """
        Process events in a separate thread so that input thread is not
        blocked.
        """
        while self.alive:
            try:
                self.handle_event(self.events.get())
            except:
                logging.exception('_run_event')

    def handle_line(self, line):
        """
        Handle input from serial port, check for events.
        """
        if line.endswith('#'):
            self.events.put(line)
        else:
            self.responses.put(line)

    def handle_event(self, event):
        """
        Spontaneous message received.
        """
        print('event received:', event)

    def command(self, command, response='OK', timeout=5):
        """
        Set an AT command and wait for the response.
        """
        with self.lock:  # ensure that just one thread is sending commands at once
            self.write_line(command)
            lines = []
            while True:
                try:
                    line = self.responses.get(timeout=timeout)
                    #~ print("%s -> %r" % (command, line))
                    if line == response:
                        return lines
                    else:
                        lines.append(line)
                except queue.Empty:
                    raise CommException('timeout ({!r})'.format(command))

    def command_with_event_response(self, command):
        """Send a command that responds with '+...' line"""
        with self.lock:  # ensure that just one thread is sending commands at once
            self._awaiting_response_for = command
            self.transport.write(b'{}\r\n'.format(command.encode(self.ENCODING, self.UNICODE_HANDLING)))
            response = self.event_responses.get()
            self._awaiting_response_for = None
            return response

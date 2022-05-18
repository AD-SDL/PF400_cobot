import os.path
import time
import logging

import zmq
import struct

import rpl_arm

def listener(host, port):
    
    try:
        ctx = zmq.Context()
        sock = ctx.socket(zmq.REP)
        sock.bind("tcp://"+host+":"+ port)
        # logger.info("Starting the command transfer listener")

        robot = rpl_arm()
        i = 1
        while True:
            msg = sock.recv_string()
            i += 1
            time.sleep(1)
            if msg != None:
                msg_output = robot.command_handler(msg)
                sock.send_string(str(msg_output))
                # sock.send_string(msg_output + '@' + msg_error + '@' + str(msg_returncode))
    
    except struct.error as e:
        # self.logger.error('Lost connection from:', sock)
        # sockClient.shutdown(socket.SHUT_RDWR)
        sock.close()

    except KeyboardInterrupt:
        # self.logger.warn('Shutting down socket')
        # sockClient.shutdown(socket.SHUT_RDWR)
        sock.close()
        exit()

if __name__ == "__main__":
    listener("*", "8085")
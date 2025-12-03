import ctypes
import subprocess

import psutil
import win32gui, win32con, win32api


class JIVLogic:
    def __init__(self):
        pass

    @staticmethod
    def is_admin():
        """Checking whether programme has administrator privilege"""

        authority = ctypes.windll.shell32.IsUserAnAdmin()
        return bool(authority)

    @staticmethod
    def get_studentmain_state():
        state = subprocess.run("tasklist|find /i \"studentmain.exe\"", shell=True).returncode
        # print(not state)
        return not state

    @staticmethod
    def set_window_top_most(hwnd):
        win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST,
                              0, 0, 0, 0,
                              win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)

    @staticmethod
    def taskkill(process_name):
        state = subprocess.run(['TASKKILL', '-F', '-IM', process_name, '-T']).returncode

        if state == 0:
            return True
            # self.logger.info(f'The process ({process_name}) has been terminated (Return code {state})')

        elif state == 128:
            return False
            # self.logger.warning(f'The process ({process_name}) not found (Return code {state})')

        elif state == 1:
            return False
            # self.logger.warning(
                # f'The process ({process_name}) could not be terminated (Return code {state})')

        else:
            return False
            # self.logger.warning(f'Unknown Error (Return code {state})')

    @staticmethod
    def get_pid_form_process_name():
        pid = None
        pids = psutil.process_iter()
        for p in pids:
            if p.name().lower() == "studentmain.exe":
                pid = psutil.Process(p.pid)
                break

        return pid


import cmd
import getpass
import sys

import netmiko


class Shell(cmd.Cmd):
    def __init__(self, *args, **kwargs):
        self.username = input("Username: ").strip()
        self.password = getpass.getpass()
        self.conn = None
        super().__init__(*args, **kwargs)
        self._set_disconnected()

    intro = "Welcome to ssh alternative.   Type help or ? to list commands.\n"
    file = None

    def _set_disconnected(self):
        self.prompt = "disconnected> "

    def do_CONNECT(self, host):
        try:
            self.conn = netmiko.ConnectHandler(
                host=host,
                username=self.username,
                password=self.password,
                device_type="cisco_ios",
            )
            hostname = self.conn.find_prompt()
            self.prompt = f"{host} - {hostname}> "

        except Exception as exc:
            print(f"Exception: {type(exc).__name__}: {exc!s}")
            self.conn = None
            self._set_disconnected()

    def default(self, command):
        if self.conn is None:
            print("not connected")
            return
        results = self.conn.send_command(command)
        print(results)

    def emptyline(self):
        pass

    def do_EOF(self, arg):
        print("")
        return True

    def do_EXIT(self, arg):
        return True


if __name__ == "__main__":
    Shell().cmdloop()

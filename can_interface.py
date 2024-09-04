import obd

class CANInterface:
    def __init__(self):
        self.connection = obd.OBD()

    def read_data(self):
        cmd = obd.commands.RPM  # Example command to read RPM
        response = self.connection.query(cmd)
        return response.value if response.is_successful else None

    def available_commands(self):
        return self.connection.supported_commands

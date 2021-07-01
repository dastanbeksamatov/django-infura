# class that represents Ethereum transaction
class Transaction:
    def __init__(self, to, data, gas, schedule):
        self.to = to
        self.data = data
        self.gas = gas
        self.schedule = schedule

    # get signature payload
    def get_payload(self, chain_id):
        return [self.to, self.data, self.gas, chain_id, self.schedule]
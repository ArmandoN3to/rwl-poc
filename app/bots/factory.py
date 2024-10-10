from app.bots.adder import AdderBot
from app.bots.printer import PrinterBot
from app.bots.subtractor import SubtractorBot
from app.bots.multiplier import MultiplierBot

class FactoryBot:

    ADDER = "ADDER"
    PRINTER = "PRINTER"
    SUBTRACTOR = "SUBTRACTOR"
    MULTIPLIER = "MULTIPLIER"
    #TODO: Implement the other bots

    @staticmethod
    def create(bot):
        if bot == FactoryBot.ADDER:
            return AdderBot()
        elif bot == FactoryBot.PRINTER:
            return PrinterBot()
        elif bot == FactoryBot.SUBTRACTOR:
            return SubtractorBot()
        elif bot == FactoryBot.MULTIPLIER:
            return MultiplierBot()
        
        #TODO: Implement the other bots
        #subtracter
        else:
            raise Exception("{bot} not found!")
        
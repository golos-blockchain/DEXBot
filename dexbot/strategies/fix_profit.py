from dexbot.decorators import check_last_run
from dexbot.strategies.base import StrategyBase
from dexbot.strategies.config_parts.fix_config import FixConfig

STRATEGY_NAME = 'Fix Profit'


class Strategy(StrategyBase):
    def __init__(self, *args, **kwargs):
        # Initializes StrategyBase class
        super().__init__(*args, **kwargs)

        self.log.info("Initializing {}...".format(STRATEGY_NAME))

        self.check_interval = 1

        # Tick counter
        self.counter = 0

        # Define Callbacks
        self.onMarketUpdate += self.maintain_strategy
        self.ontick += self.tick

        self.error_ontick = self.error
        self.error_onMarketUpdate = self.error
        self.error_onAccount = self.error

        # Get view
        self.view = kwargs.get('view')

        self.worker_name = kwargs.get('name')

        self.log.info("{} initialized.".format(STRATEGY_NAME))

    @classmethod
    def configure(cls, return_base_config=True):
        return FixConfig.configure(return_base_config)

    @classmethod
    def configure_details(cls, include_default_tabs=True):
        return FixConfig.configure_details(include_default_tabs)

    @check_last_run
    def maintain_strategy(self, *args):
        self.log.info('ms')
        pass

    def error(self, *args, **kwargs):
        """Defines what happens when error occurs."""
        self.disabled = True

    def tick(self, block_hash):
        """Ticks come in on every block."""
        if not (self.counter or 0) % 3:
            self.maintain_strategy()
        self.counter += 1

from dexbot.strategies.config_parts.base_config import BaseConfig, ConfigElement, ConfigMessageElement


class FixConfig(BaseConfig):
    @classmethod
    def configure(cls, return_base_config=True):
        def sell_msg(worker_config):
            return str(float(worker_config['buy']) * (100 + float(worker_config['spread'])) / 100)
        config = [
            ConfigElement(
                'fbo_price',
                'float',
                0,
                'First buy order price',
                '',
                (0, 10000000, 8, ''),
            ),
            ConfigElement(
                'buy',
                'float',
                100,
                'Fixed buy order size',
                '',
                (0, 10000000, 8, ''),
            ),
            ConfigElement(
                'spread', 'float', 5, 'Spread', 'The percentage difference between buy and sell', (0, 100, 2, '%')
            ),
            ConfigMessageElement(
                'sell',
                'First sell order size (calculated) is',
                sell_msg
            ),
            ConfigElement(
                'inc', 'float', 2, 'Increment', 'The percentage difference between 2 sequence order prices', (0, 100, 2, '%')
            )
        ]

        return BaseConfig.configure(return_base_config) + config

    @classmethod
    def configure_details(cls, include_default_tabs=True):
        return BaseConfig.configure_details(include_default_tabs) + []

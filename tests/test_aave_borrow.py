from brownie import config, network
from scripts.aave_borrow import (
    approve_erc20,
    get_lending_pool,
    get_asset_price,
    get_account,
)


def test_get_asset_price():
    asset_price = get_asset_price(
        config["networks"][network.show_active()]["dai_eth_price_feed"]
    )
    assert asset_price > 0


def test_approve_erc20():
    account = get_account()
    lending_pool = get_lending_pool()
    amount = 1000000000000000000
    erc20_address = config["networks"][network.show_active()]["weth_token"]

    tx = approve_erc20(amount, lending_pool.address, erc20_address, account)
    tx.wait(1)

    assert tx is not True


def test_get_lending_pool():
    lending_pool = get_lending_pool()

    assert lending_pool is not None

from brownie import accounts, config, SimpleStorage, network

# import os


def deploy_simple_storage():
    # 1. => add accounts with Brownie's "default" local ganache-cli accounts
    # account = accounts[0]
    # print(account)

    # 2. => add my accounts with Brownie's encrypted command line storage
    # account = accounts.load("metamaskTestAccount")
    # print(account)

    # 3. => add my accounts with OS environement variable (.env) + import OS
    # account = accounts.add(os.getenv("PRIVATE_KEY_METAMASK"))
    # print(account)

    # 4. => add my accounts with OS environement variable pulled from brownie-config.yaml
    # account = accounts.add(config["wallets"]["from_key"])
    # print(account)

    account = get_account()

    simple_storage = SimpleStorage.deploy({"from": account})
    print(simple_storage)
    stored_value = simple_storage.retrieve()
    print(stored_value)
    transaction = simple_storage.store(15, {"from": account})
    transaction.wait(1)
    updated_stored_value = simple_storage.retrieve()
    print(updated_stored_value)


def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def main():
    deploy_simple_storage()

def profile_contract(contract):

    print("Name: ", contract.compiler_data.contract_name)
    print("Address: ", contract.address)
    print("Bytecode: ", contract.bytecode)

    print("Storage layout:")
    for var_name, storage_location in contract.compiler_data.storage_layout[
        "storage_layout"
    ].items():
        print(
            "\t {} with type {} at slot {}".format(
                var_name, storage_location["type"], storage_location["slot"]
            ),
        )

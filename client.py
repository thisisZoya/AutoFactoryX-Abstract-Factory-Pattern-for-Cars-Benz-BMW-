def client_code(factory):
    suv = factory.create_suv()
    coupe = factory.create_coupe()

    print(suv.drive())
    print(coupe.drive())

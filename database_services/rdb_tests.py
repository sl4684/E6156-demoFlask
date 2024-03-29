from database_services.RDBService import RDBService


def t1():

    res = RDBService.get_by_prefix(
        "imdb", "names_basic", "primary_name", "Tom H"
    )
    print("t1 results = ", res)


def t2():

    res = RDBService.find_by_template(
        "imdb", "name_basics", {"primary_name": "Tom Hanks"}, None
    )
    print("t2 results = ", res)


def t3():

    res = RDBService.create(
        "aaaaf21", "addresses",
            {
                "address1": "520 w 120th St",
                "city": "New York",
                "region": "NY",
                "country": "USA",
                "postal_code": "10027"
            })
    print("t3: res = ", res)

t2()
#t3()



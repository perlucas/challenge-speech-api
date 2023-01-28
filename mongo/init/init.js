db.createUser(
    {
        user: "tester",
        pwd:  "tester",
        roles: [
            { role: "readWrite", db: "test" }
        ]
    }
);
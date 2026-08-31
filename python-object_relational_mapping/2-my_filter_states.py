query = (
    "SELECT * FROM states "
    "WHERE BINARY name = %s "
    "ORDER BY id ASC"
)

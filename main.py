import sqlite3

import connectSql
import loginPage


def main():
    loginPage.LoginPage()
    # Run Main
    loginPage.tk.mainloop()



if __name__ == '__main__':
    conn = connectSql.Connection()
    main()

    #main(conn)

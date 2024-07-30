from app import mainApp
from first_page import firstPage

def main():
    app = mainApp(width=400, height=550)
    firstPage(app)
    app.mainloop()

if __name__ == '__main__':
    main()
def main():
    create_page = open('main.html', 'w')
    name = input("Enter your full name: ")
    record_about_user = input("Here you can to write smt about yourself: ")
    create_page.write("<html>\n"
                      "<head>\n"
                      "</head>\n"
                      "<body>\n"
                      "\t<center>\n"
                      "\t<h1>" + name + "</h1>\n"
                                        "\t</center>\n"
                                        "\t<hr />" + record_about_user + "<hr />\n"
                                                                         "</body>\n"
                                                                         "</html>")
    create_page.close()


main()
#import TK
from tkinter import *
import os
import subprocess



class Splash(Tk):
    def __init__(self):
        Tk.__init__(self)

        self.Format = StringVar()
        
        #title of GUI
        self.title("Citation Generator")
        #creating the layout of the GUI
        self.lblType = Label(self, text = "What type of citation?")
        self.lblType.grid(row = 0, columnspan = 4)

        self.radWebsite = Radiobutton(self, text = "Website", value = '1', variable = self.Format)
        self.radWebsite.grid(row = 1, column = 1)

        self.radBook = Radiobutton(self, text = "Book", value = '2', variable = self.Format)
        self.radBook.grid(row = 1, column = 2)
        #sets initial value to Website
        self.Format.set('1')

        self.butBegin = Button(self, text = "Begin", command = self.Begin)
        self.butBegin.grid(row = 4, columnspan = 4)

        self.mainloop()
    #determines which GUI opens
    def Begin(self):
        if self.Format.get() == '1':
            self.Close()
            Website()          
        elif self.Format.get() == '2':
            self.Close()
            Book()
    #closes Splash GUI 
    def Close(self):
        self.destroy()

           

        
class Website(Tk):
    def __init__(self):
        Tk.__init__(self)

        self.MLAorAPA = StringVar()
        
        #layout of Website GUI
        self.title("Citation Generator")

        self.lblTitle = Label(self, text = "Website")
        self.lblTitle.grid(row = 0, columnspan = 4)

        self.lblWebsiteTitle = Label(self, text = "Website Title:")
        self.lblWebsiteTitle.grid(row = 1, column = 1)
        self.txtWebsiteTitle = Entry(self)
        self.txtWebsiteTitle.grid(row = 1, column = 2)

        self.lblArticle = Label(self, text = "Article Title:")
        self.lblArticle.grid(row = 2, column = 1)
        self.txtArticle = Entry(self)
        self.txtArticle.grid(row = 2, column = 2)

        self.lblAuthorLast = Label(self, text = "Author Last Name:")
        self.lblAuthorLast.grid(row = 3, column = 1)
        self.txtAuthorLast = Entry(self)
        self.txtAuthorLast.grid(row = 3, column = 2)

        self.lblAuthorFirst = Label(self, text = "Author First Name:")
        self.lblAuthorFirst.grid(row = 4, column = 1)
        self.txtAuthorFirst = Entry(self)
        self.txtAuthorFirst.grid(row = 4, column = 2)

        self.lblPublisher = Label(self, text = "Publisher:")
        self.lblPublisher.grid(row = 5, column = 1)
        self.txtPublisher = Entry(self)
        self.txtPublisher.grid(row = 5, column = 2)

        self.lblURL = Label(self,text = "Website URL:")
        self.lblURL.grid(row = 6, column = 1)
        self.txtURL = Entry(self)
        self.txtURL.grid(row = 6, column = 2)

        self.lblDatePublished = Label(self, text = "Date Published")
        self.lblDatePublished.grid(row = 7, columnspan = 4)

        self.lblYearPublished = Label(self, text = "Year:")
        self.lblYearPublished.grid(row = 8, column = 1)
        self.txtYearPublished = Entry(self)
        self.txtYearPublished.grid(row = 8, column = 2)

        self.lblMonthPublished = Label(self, text = "Month:")
        self.lblMonthPublished.grid(row = 9, column = 1)
        self.txtMonthPublished = Entry(self)
        self.txtMonthPublished.grid(row = 9, column = 2)

        self.lblDayPublished = Label(self, text = "Day:")
        self.lblDayPublished.grid(row = 10, column = 1)
        self.txtDayPublished = Entry(self)
        self.txtDayPublished.grid(row = 10, column = 2)

        self.lblDateAccessed = Label(self, text = "Date Accessed")
        self.lblDateAccessed.grid(row = 11, columnspan = 4)

        self.lblYearAccessed = Label(self, text = "Year:")
        self.lblYearAccessed.grid(row = 12, column = 1)
        self.txtYearAccessed = Entry(self)
        self.txtYearAccessed.grid(row = 12, column = 2)

        self.lblMonthAccessed = Label(self, text = "Month:")
        self.lblMonthAccessed.grid(row = 13, column = 1)
        self.txtMonthAccessed = Entry(self)
        self.txtMonthAccessed.grid(row = 13, column = 2)

        self.lblDayAccessed = Label(self, text = "Day:")
        self.lblDayAccessed.grid(row = 14, column = 1)
        self.txtDayAccessed = Entry(self)
        self.txtDayAccessed.grid(row = 14, column = 2)

        self.radMLA = Radiobutton(self, text = "MLA", value = '1', variable = self.MLAorAPA, command = self.SetMLA)
        self.radMLA.grid(row = 16, column = 1)
        self.radAPA = Radiobutton(self, text = "APA", value = '2', variable = self.MLAorAPA, command = self.SetAPA)
        self.radAPA.grid(row = 16, column = 2)
        self.MLAorAPA.set('1')
        
        
        self.btnCite = Button(self, text = "Cite", command = self.CiteWebsite)
        self.btnCite.grid(row = 17, columnspan = 4)

        self.lblCitation = Label(self, text = ' ')
        self.lblCitation.grid(row = 18, columnspan = 4)

        self.mainloop()
    #sets variable manually(it wasn't working correctly through radiobutton)
    def SetMLA(self):
        self.MLAorAPA.set('1')

    def SetAPA(self):
        self.MLAorAPA.set('2')
    #puts strings in appropriate places
    def CiteWebsite(self):
        WebsiteTitle = self.txtWebsiteTitle.get()
        Article = self.txtArticle.get()
        AuthorLast = self.txtAuthorLast.get()
        AuthorFirst = self.txtAuthorFirst.get()
        Publisher = self.txtPublisher.get()
        URL = self.txtURL.get()
        YearPublished = self.txtYearPublished.get()
        MonthPublished = self.txtMonthPublished.get()
        DayPublished = self.txtDayPublished.get()
        YearAccessed = self.txtYearAccessed.get()
        MonthAccessed = self.txtMonthAccessed.get()
        DayAccessed = self.txtDayAccessed.get()
        keepgoing = True

        File_Write = open("Bibliography.txt", 'a')
        #determines MLA or APA            
        if self.MLAorAPA.get() == '1':
            File_Write.write('{}, {}. "{}." {}, {} {} {}, {}. Accessed {} {} {}.\n'.format(
            AuthorLast, AuthorFirst, Article, WebsiteTitle, DayPublished, MonthPublished,
            YearPublished, URL, DayAccessed, MonthAccessed, YearAccessed))

        elif self.MLAorAPA.get() == '2':
            File_Write.write('{}, {}. ({}, {} {}). {}.  Retrieved from {}\n'.format(
            AuthorLast, AuthorFirst, YearPublished, MonthPublished, DayPublished, Article,
            URL))

        
        #asks if user wants to make another citation
        retry = messagebox.askyesno('', "Would you like to make another citation?")

        if retry == True:
            self.Close()
            Splash()
        elif retry == False:
            self.Close()
            File_Write.close()
            
    def Close(self):
        self.destroy()
        


class Book(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Citation Generator")
        #layout of GUI for Book
        self.APAorMLA = StringVar()

        self.lblTitle = Label(self, text = "Book")
        self.lblTitle.grid(row = 0, columnspan = 4)

        self.lblBookTitle = Label(self, text = "Book Title:")
        self.lblBookTitle.grid(row = 1, column = 1)
        self.txtBookTitle = Entry(self)
        self.txtBookTitle.grid(row = 1, column = 2)

        self.lblAuthorLast = Label(self, text = "Author Last Name:")
        self.lblAuthorLast.grid(row = 3, column = 1)
        self.txtAuthorLast = Entry(self)
        self.txtAuthorLast.grid(row = 3, column = 2)

        self.lblAuthorFirst = Label(self, text = "Author First Name:")
        self.lblAuthorFirst.grid(row = 4, column = 1)
        self.txtAuthorFirst = Entry(self)
        self.txtAuthorFirst.grid(row = 4, column = 2)

        self.lblPublisher = Label(self, text = "Publisher:")
        self.lblPublisher.grid(row = 5, column = 1)
        self.txtPublisher = Entry(self)
        self.txtPublisher.grid(row = 5, column = 2)

        self.lblPublicationCity = Label(self,text = "City of Publication:")
        self.lblPublicationCity.grid(row = 6, column = 1)
        self.txtPublicationCity = Entry(self)
        self.txtPublicationCity.grid(row = 6, column = 2)

        self.lblPublicationYear = Label(self, text = "Year of Publication:")
        self.lblPublicationYear.grid(row = 8, column = 1)
        self.txtPublicationYear = Entry(self)
        self.txtPublicationYear.grid(row = 8, column = 2)

        self.lblVolumeNumber = Label(self, text = "Volume Number:")
        self.lblVolumeNumber.grid(row = 9, column = 1)
        self.txtVolumeNumber = Entry(self)
        self.txtVolumeNumber.grid(row = 9, column = 2)

        self.radMLABook = Radiobutton(self, text = "MLA", value = '1', variable = self.APAorMLA, command = self.setMLABook)
        self.radMLABook.grid(row = 10, column = 1)
        self.radAPABook = Radiobutton(self, text = "APA", value = '2', variable = self.APAorMLA, command = self.setAPABook)
        self.radAPABook.grid(row = 10, column = 2)
        self.APAorMLA.set('1')

        self.btnCite = Button(self, text = "Cite", command = self.CiteBook)
        self.btnCite.grid(row = 15, columnspan = 4)

        self.lblCitation = Label(self, text = ' ')
        self.lblCitation.grid(row = 16, columnspan = 4)
    #manually sets value for radio button again
    def setMLABook(self):
        self.APAorMLA.set('1')

    def setAPABook(self):
        self.APAorMLA.set('2')
    #Cites the Book selection
    def CiteBook(self):
        Title = self.txtBookTitle.get()
        LastName = self.txtAuthorLast.get()
        FirstName = self.txtAuthorFirst.get()
        Publisher = self.txtPublisher.get()
        City = self.txtPublicationCity.get()
        Date = self.txtPublicationYear.get()
        Volume = self.txtVolumeNumber.get()
        Medium = "Print"
        #opens file to write to
        File_Write = open("Bibliography.txt", 'a')
        #determines APA or MLA style
        if self.APAorMLA.get() == '1':
            File_Write.write("{},{}. {}. {}: {}, {}. {}.\n".format(
                LastName, FirstName, Title, City, Publisher, Date, Medium))
                   
        elif self.APAorMLA.get() == '2':
            File_Write.write("{}, {}. ({}). {}. {}: {}.\n".format(
                LastName, FirstName[0],Date, Title, City, Publisher))
        #asks if user would like to make another citation
        retry = messagebox.askyesno('', "Would you like to make another citation?")

        if retry == True:
            self.Close()
            Splash()
        elif retry == False:
            self.Close()
            File_Write.close()
    #closes program if user desires           
    def Close(self):
        self.destroy()

               
        
            
def main():
    Splash()

if __name__ == '__main__':
    main()

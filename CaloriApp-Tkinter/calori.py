# -*- coding: UTF-8 -*-

from Tkinter import *

import ttk

import csv

class Food:
    # in this class we created to give objects to the items
    def __init__(self, calori, name, price):
        self.calori = calori
        self.name = name
        self.price = price


class Methods():
    def __init__(self):
        # here we initialized the variables
        self.added_food = []
        self.added_food2 = []
        self.food_write = ""
        self.file_number = int()

    def taking_csv(self):
        # here we opent and write a new csv file and we write the items have choosen
        with open(self.path_entry.get()) as self.csv_file:
            # csv_reader = csv.reader(csv_file, delimiter=',')
            self.csv_reader = csv.DictReader(self.csv_file)
            self.items_dict = {}
            for row in self.csv_reader:
                self.ooo = row.keys()
                # here we r giving obejcts to the classes
                self.items_dict[row["Calories"]] = Food(row["Calories"], row["Name"], row["Price"])

            self.list1 = []
            self.o1 = self.ooo[1] + "," + self.ooo[2] + "," + self.ooo[0]

            self.list_of_food.insert(0, self.o1)

            for u in self.items_dict.values():
                # in this loop we r taking the food and thier price and calori
                self.list1.append(str(u.calori) + "," + u.name + "," + str(float(u.price)))

            for i in self.list1:
                # here we r putting to the list box

                self.list_of_food.insert(END, i)

    def add_food(self):
        # in this function we r adding from listbox to the another listbox
        try:
            #  we r taking one by one
            selection = self.list_of_food.curselection()
            for i in selection:
                selected_food = self.list_of_food.get(i)
                if selected_food != self.o1:
                    self.added_food.append(selected_food)
                    if self.added_food not in self.added_food2:
                        # here we r putting to the my_food listbox
                        self.my_food.insert(END, selected_food)
                        self.added_food2.append(selected_food)
                else:
                    pass
        except:
            pass

    def do_remove_food(self):
        #  in this function we r removing the items from my_food listbox
        remove = self.my_food.curselection()
        removeList = self.my_food.get(remove)
        self.my_food.delete(remove)
        self.added_food2.remove(removeList)

    def calculate_calori(self):
        # this function just calculate the sum of the calories have choosen
        self.sum = 0
        self.orders = 0
        for i in self.added_food2:
            self.sum += int(i.split(",")[0])

    def write_csv_txt(self):
        # here we opent a file and have taken the items from the file

        self.file_number = self.var2.get()
        if self.file_number == 2:
            with open('my_food.csv', mode='w') as my_choices:
                rows = ["Your_Order", "Calori", "Price", "Total"]
                writer = csv.DictWriter(my_choices, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL,
                                        fieldnames=rows)
                writer.writeheader()
                for ii in self.added_food2:
                    self.pp = ii.split(",")[1].encode("utf-8")

                    writer.writerow(
                        {'Your_Order': self.pp, 'Calori': int(ii.split(",")[0]), 'Price': float(ii.split(",")[2]),
                         'Total': self.sum})
        else:
            # in here we r wrint a txt file
            self.my_choices2 = open("my_food.txt", "w")
            for iii in self.added_food2:
                self.my_choices2.write("Your Order is {}, ".format(iii.split(",")[1].encode("utf-8")))
                self.my_choices2.write("Calori is {}, ".format(int(iii.split(",")[0])))
                self.my_choices2.write("Price is {}, ".format(float(iii.split(",")[2])))
                self.my_choices2.write("Total is {}\t\n".format(self.sum))


class Widgets(Frame, Methods):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        Methods.__init__(self)
        self.initUI(parent)
        self.frame1 = Frame()
        self.frame2 = Frame()
        self.diet_text = int()

    #     in summary i created 3 frames to put the widgets and they appear in order to clixk the continue buttton

    def initUI(self, parent):
        self.grid()
        self.label_head = Label(self, text='Sehir Cafeteria', fg='red', font=('', '20', 'bold'), bg="blue", width=47)
        self.label_head.grid(row=0, column=0, columnspan=14)
        self.path_label = Label(self, text='File path', font=('', '14', "bold"))
        self.path_label.grid(row=1, column=0, sticky=W)
        self.path_entry = Entry(self, width=50, text="")
        self.path_entry.grid(row=1, column=1)
        self.diet_label = Label(self, text='Choose your diet', fg='black', font=('', '15', 'bold'))
        self.diet_label.grid(row=2, column=0, sticky=W)
        self.var = IntVar()

        self.radiou_buttons = Radiobutton(self,
                                          text="1300 kcl",
                                          variable=self.var,
                                          value=1)
        self.radiou_buttons.grid(row=2, column=1)
        self.radiou_buttons2 = Radiobutton(self,
                                           text="1800 kcl",
                                           variable=self.var,
                                           value=2)
        self.radiou_buttons2.grid(row=2, column=3)

        self.radiou_buttons3 = Radiobutton(self,
                                           text="2300 kcl",
                                           variable=self.var,
                                           value=3)
        self.radiou_buttons3.grid(row=2, column=4)

        self.continue1 = Button(self, width=18, text="Continue", font=(" ", "10", "bold"), fg="black", bg="red",
                                command=self.initUI2)
        self.continue1.grid(row=4, column=0, sticky=W)

        self.diet_choice = Label(self, text='Your diet is', font=('', '16', 'bold'), fg="black")
        self.diet_choice.grid(row=3, column=0, sticky=W)

    def initUI2(self):
        self.frame1.grid()
        self.diet_number = self.var.get()
        if self.diet_number == 1:
            self.diet_text = 1300
        elif self.diet_number == 2:
            self.diet_text = 1800
        elif self.diet_number == 3:
            self.diet_text = 2300

        self.diet_choice.config(text='Your diet is %d' % self.diet_text)
        self.label_head = Label(self.frame1, fg='white', font=('', '17', 'bold'), bg="white",
                                width=50)
        self.label_head.grid(row=0, column=0, pady=3)
        self.food_label = Label(self.frame1, text='Choose Your Food', font=('', '14', "bold"))
        self.food_label.grid(row=1, column=0)
        self.food_menu_label = Label(self.frame1, text="Food Menu", font=('', '14', "bold"))
        self.food_menu_label.grid(row=2, column=0, sticky=W, padx=30)
        self.list_of_food = Listbox(self.frame1, bg="white", width=30, height=14)
        self.list_of_food.grid(row=3, column=0, sticky=W)
        self.add_food = Button(self.frame1, width=10, text="Add Food", font=(" ", "10", "bold"), fg="black", bg="red",
                               command=self.add_food)
        self.add_food.grid(row=4, column=0)
        self.remove_food = Button(self.frame1, width=10, text="Remove Food", font=(" ", "10", "bold"), fg="black",
                                  bg="red",
                                  command=self.do_remove_food)
        self.remove_food.grid(row=5, column=0)

        self.my_food_label = Label(self.frame1, text="My Food", font=('', '14', "bold"))
        self.my_food_label.grid(row=2, column=0, sticky=E, padx=(0, 30))

        self.my_food = Listbox(self.frame1, bg="white", width=30, height=14)
        self.my_food.grid(row=3, column=0, sticky=E)
        self.continue2 = Button(self.frame1, width=10, text="Continue", font=(" ", "10", "bold"), fg="black", bg="red",
                                command=self.initUI3)
        self.continue2.grid(row=6, column=0, sticky=W)
        self.taking_csv()

    def initUI3(self):
        self.frame2.grid()
        self.calculate_calori()

        self.summary_label = Label(self.frame2, text='Summmary and Data Saving', font=('', '14', "bold"))
        self.summary_label.grid(row=1, column=0)

        self.summary_label2 = Label(self.frame2, text='Your Diet Choice is %d' % self.diet_text,
                                    font=('', '12', "bold"))
        self.summary_label2.grid(row=2, column=0, sticky=W)

        self.summary_label3 = Label(self.frame2, fg='black', font=('', '11', 'bold'), bg="red", text="",

                                    width=50)
        self.summary_label3.grid(row=3, column=0, sticky=W)
        if self.sum <= self.diet_text:
            self.summary_label3.config(text="Your Chosen Food Menu-Amount of Calories:%d kcal" % self.sum, bg="green")

        elif self.sum > self.diet_text:
            self.summary_label3.config(
                text="Your Chosen Food Menu-Amount of Calories:%d kcal above daily limit" % self.sum)
        self.choose_type = Label(self.frame2, text='Choose File Type:', font=('', '12', "bold"))
        self.choose_type.grid(row=4, column=0, sticky=W)

        self.var2 = IntVar()

        self.radiou_type = Radiobutton(self.frame2,
                                       text="Txt File",
                                       variable=self.var2,
                                       value=1)
        self.radiou_type.grid(row=4, column=1, sticky=W)

        self.radiou_type2 = Radiobutton(self.frame2,
                                        text="CSV File",
                                        variable=self.var2,
                                        value=2)
        self.radiou_type2.grid(row=4, column=2, sticky=W)

        self.save_file = Button(self.frame2, width=10, text="Save File", font=(" ", "10", "bold"), fg="black", bg="red",
                                command=self.write_csv_txt)
        self.save_file.grid(row=4, column=3, sticky=W)


def main():
    if __name__ == '__main__':
        root = Tk()
        root.title('tk')
        app = Widgets(root)
        # app.pack(expand=True)
        root.mainloop()


main()
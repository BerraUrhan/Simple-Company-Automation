# THE EVIL THE CAPITALIST THE RULER CORPORATİON AUTOMATİON or just an automation jajaja

class corporation:
    def __init__(self,name):
        self.name = name
        self.workit = True

    def msg_box(self,thing = "welcome"): # giriş cümlesi
        wel = f"Welcome to {self.name} corporation. "
        bye = f"-- Presented by {self.name} corporation --"
        row = len(wel)
        row2 = len(bye)
        h = " ".join(["X"]+["="* row]+["X"])
        h2 = " ".join(["X"]+["="* row2]+["X"])

        result = h + "\n" + "| " + wel + " |"+ "\n" + h
        result2 = h2 + "\n" + "| " + bye + " |" + "\n" + h2
        if thing == "welcome":
            print(result)
        else:
            print(result2)


    def program(self):
        option = self.menuOption()
        if option == 1:
            self.addStaff()
        if option == 2:
            self.delStaff()
        if option == 3:
            type = input("press y to see salary per a year / press a to see salary per a month --> ")
            if type == "y":
                self.salary(type="y")
            else:
                self.salary(type="a")
        if option == 4:
            self.budget()
        if option == 5:
            self.income()
        if option == 6:
            self.outlay()
        if option == 7:
            self.theend()

# ---------------------------------------------------------------------------

    def menuOption(self): # main fonksiyon olsun, seçimler yapılsın
        #self.msg_box()
        option = int(input("\n\n"
                            "1 - Add Staff\n"
                            "2 - Remove Staff\n"
                            "3 - Show salary to give\n"
                            "4 - Show budget\n"
                            "5 - Enter income\n"
                            "6 - Enter outlay\n"
                            "7 - End the process\n\n "
                            "Please choose the operation : "))
        while option < 1 or option > 7:
            option = int(input("Please enter a value between 1-7 : "))
        return option
# ---------------------------------------------------------------------------------
    def addStaff(self):
        nameS = input("Enter staff's name : ")
        surname = input("Enter staff's surname : ")
        age = input("Enter staff's age : ")
        gender = input("Enter staff's gender : ")
        salaryS = input("Enter staff's name salaryS : ")


        with open("staff.txt","r",encoding = "utf-8") as f:
            staffList = f.readlines() # satır satır çalışan listesi
        with open("staff.txt","r",encoding = "utf-8") as f:
            if len(staffList) == 0:
                id = 1
            else :
                id = int(f.readlines()[-1].split(")")[0]) + 1

        with open("staff.txt","a+",encoding = "utf-8") as f:
            f.write(f"{id}){nameS}--{surname}--{age}--{gender}--{salaryS}\n")
#-----------------------------------------------------------------------------------

    def delStaff(self):
    # çalışan listesi göster- input al
        with open("staff.txt","r",encoding = "utf-8") as f:
            staffList = f.readlines() # satır satır çalışan listesi

        nstaffL = []  # güncel çalışan listesi
        for staff in staffList:
            nstaffL.append(" ".join(staff[:-1].split("--")))

        for ele in nstaffL: # staff list before (çıkarılacak adam listesini gösteriyor )
            print(ele)

        who = int(input(f"\nPlease select the staff you want to remove (1-{len(nstaffL)}): \n"))
        if len(staffList) != 0:
            staffList.pop(who-1) # pop indexle çıkarır
        else:
            print("There is not any employee")
            a.program()

    # ----- dosyayı idlerle yeniden yazmak -----
        changedStaff = []
        counter = 1
        for ele in staffList:
            changedStaff.append(str(counter) +")"+ ele.split(")")[1])
            counter += 1 # yeni id
        for ele in changedStaff:  # staff list after
            print(" ".join(ele[:-1].split("--"))) # estetik göstermesi için

        with open("staff.txt", "w", encoding="utf-8") as f:
            f.writelines(changedStaff)
# -----------------------------------------------------------------------------------
    def salary(self,type = "a"): # verilecek toplam maaş
        # type m ise per month , y ise per year
        with open("staff.txt","r",encoding = "utf-8") as f:
            staffList = f.readlines() # satır satır çalışan listesi
            maaslar = []
            for ele in staffList:
                maaslar.append(int(ele.split("--")[-1]))
            if type == "a":
                month = sum(maaslar)
                print(f"The salary you should give per month is : {month}")
            else:
                year = sum(maaslar)*12
                print(f"The salary you should give per year is : {year}")
# -----------------------------------------------------------------------------------

    def budget(self):
        with open("staff.txt","r",encoding = "utf-8") as f:
            staffList = f.readlines() # satır satır çalışan listesi
            maaslar = []
            for ele in staffList:
                maaslar.append(int(ele.split("--")[-1]))
            toplamMaaslar = sum(maaslar)
            with open("budget.txt","r") as f:
                allBudget = int(f.readlines()[0])

            print(f"Your budget before giving salarys is : {allBudget}")
            allBudget -= toplamMaaslar
            print(f"Your budget after giving salarys is : {allBudget}")

            with open("budget.txt","w") as f:
                f.write(str(allBudget))

    def income(self):
        pass
    def outlay(self):
        pass
    def theend(self):
        isEnd = input("Press 'e' to end the process --> ")
        if isEnd == "e":
            print("\n\n     Thank you for choosing us ! \n\n")
            self.msg_box(thing="bye")
            self.workit = False
        else:
            self.workit = True

a = corporation(name = "* U R H A N *")

a.msg_box()
while a.workit:
    a.program()
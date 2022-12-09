import view, model

def menu():
    data= []
    while True:
        choice = view.show_menu()
        if choice == "":
            print("See you later.")
            break
        elif choice == "1":
            rec = model.create_rec(*view.new_record())
            data.append(rec)
        elif choice == "2":
            filename = view.file_name()
            recs =  model.import_file(filename)
            data.append(recs)
        elif choice == "3":
            filename = view.file_name()
            model.update_record()
        elif choice == "4":
            view.show_record(data)
        elif choice == "6":
            filename = view.file_name()
            model.export_file(filename,data)
        else:
            print("Unknown choice")
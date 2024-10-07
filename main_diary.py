import datetime
import get_date

class diary:
    def __init__(self):
        self._entry_writing = []
        self.title = None
        self.now = datetime.datetime.now()
        self.calendar_date = datetime.datetime.now().strftime("%m_%d_%Y")
        self.digital_time = get_date.get_date_now().get_time()

    
    def entry_title(self):
        entry_title = input('Please enter the title of the diary entry: ')
        self.title = entry_title
        return self.title
    
    
    def write_entry(self):
        try:
            title = self.entry_title()

            with open(f'{title} {self.calendar_date}.txt', 'x') as entry:
                entry.write(f"{self.now.strftime('%B')} {self.now.strftime('%d')}, {self.now.strftime('%Y')}\n")
                entry.write(f'{self.now.strftime("%A")}\n')
                entry.write(f'{self.digital_time}\n')
                entry.write('\n')
                entry.write('Dear Diary,\n')
                entry.write('\n')
            #diary header

                entry.write("   ")
                first_line = input("Write the contents of the diary. Type 'quit' to stop writing: ")
                self._entry_writing.append(first_line)
                if first_line.upper() == 'QUIT':
                    print('You decided not to write anything. Sometimes things are better kept in your mind.')
                    return
            
                while True:
                    write_entry = input('Continue writing. Catharsis is medicine in of itself, you know: ')
                    if write_entry.upper() ==  'QUIT':
                        break
                    self._entry_writing.append(write_entry)

                contents = '\n'.join(self._entry_writing)
                entry.write(contents)

            print('Diary entry completed successfully.')
        except FileExistsError:
            bruh = "\U0001F5FF"
            print(f'This entry title already exists {bruh} Try creating another title.')
            print(bruh*10)


if __name__ == '__main__':
    test = diary()
    test.write_entry()
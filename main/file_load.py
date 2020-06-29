import numpy as n
import csv

class file_load:
    def __init__(self,num_files):
        self.num_files =num_files+1
        self.total_data=[]
        self.data_pop = self.run_through_files()
        self.array = self.array_format()

    def open_file(self,file_name):
        '''Enter the general file name. This command opens the file then appends the data to a list.'''
        with open(file_name, 'r') as patient_file:
            for row in csv.reader(patient_file):
                patient_data= []
                for i in row:
                    patient_data.append(i)
                self.total_data.append(patient_data)

    def run_through_files(self):
        '''Need to manually set file name here. This function loops through files and runs the open file command.'''
        for i in range(1,self.num_files):
            num = str(i).zfill(2)
            file_name = 'inflammation-{}.csv'.format(num)
            self.open_file(file_name)

    def array_format(self):
        '''Sets data as an numpy array.'''
        self.total_data = n.array(self.total_data).astype(n.float)

    

if __name__ == '__main__':
    pass

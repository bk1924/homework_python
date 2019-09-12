{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import csv\n",
    "from pathlib import Path"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Current Working Directory:/Users/jiwookkim/Desktop/python-homework/PyBank\n"
     ]
    }
   ],
   "source": [
    "print(f\"Current Working Directory:{Path.cwd()}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Financial Analysis\n",
      "-----------------------------------\n",
      "Total Months: 86\n",
      "Total : 38382578\n",
      "Average Change : $-2288.2\n",
      "Greatest Increase in Profits: Feb-2012 ($1926159)\n",
      "Worst Decrease in Profits Sep-2013 ($-2196167)\n"
     ]
    }
   ],
   "source": [
    "csvpath = Path('/Users/jiwookkim/Desktop/python-homework/PyBank/budget_data.csv')\n",
    "\n",
    "#Instantiaing variables\n",
    "months = 0\n",
    "npl = 0\n",
    "monthly_change = 0\n",
    "next_value = 0\n",
    "dates = []\n",
    "profits = []\n",
    "\n",
    "#instantiate for best and worst performance\n",
    "best_increase = 0\n",
    "worst_decrease= 0\n",
    "\n",
    "#open the csv file as an object\n",
    "with open(csvpath, 'r') as csvfile:\n",
    "    csvreader = csv.reader(csvfile)\n",
    "    \n",
    "    #read the header\n",
    "    header = next(csvreader)\n",
    "    \n",
    "    #get previous values for calculating the changes\n",
    "    previous_value = next(csvreader)\n",
    "    npl += int(previous_value[1])\n",
    "    months += 1\n",
    "    \n",
    "    #Read each row of data after the header\n",
    "    for row in csvreader:\n",
    "        \n",
    "        #into empty dates list, append date from csv Date column\n",
    "        dates.append(row[0])\n",
    "        months += 1\n",
    "        \n",
    "        #month to month change average\n",
    "        #calculating change\n",
    "        monthly_change = int(row[1]) - int(previous_value[1])\n",
    "        profits.append(monthly_change)\n",
    "        average_monthly_change = round(sum(profits) / months, 2)\n",
    "        \n",
    "        #update previous_value\n",
    "        previous_value = row\n",
    "\n",
    "        \n",
    "        #calculating total profit/losses\n",
    "        npl = npl + int(row[1])\n",
    "        \n",
    "        #monthly_change comparison\n",
    "        if monthly_change >= best_increase:\n",
    "            best_increase = monthly_change\n",
    "            best_increase_month = row[0]\n",
    "        elif monthly_change <= worst_decrease:\n",
    "            worst_decrease = monthly_change\n",
    "            worst_decrease_month = row[0]\n",
    "        \n",
    "        \n",
    "\n",
    "\n",
    "        \n",
    "        \n",
    "print(f\"Financial Analysis\")\n",
    "print(f\"-----------------------------------\")\n",
    "print(f\"Total Months: {months}\")\n",
    "print(f\"Total : {npl}\")\n",
    "print(f\"Average Change : ${average_monthly_change}\")\n",
    "print(f\"Greatest Increase in Profits: {best_increase_month} (${best_increase})\")\n",
    "print(f\"Worst Decrease in Profits {worst_decrease_month} (${worst_decrease})\")\n",
    "\n",
    "\n",
    "#Set the path for the output.csv\n",
    "output_path = Path('/Users/jiwookkim/Desktop/python-homework/PyBank/output.txt')\n",
    "\n",
    "#open the output path as a file \n",
    "with open(output_path, 'w', newline='') as file:\n",
    "    file.write(f\"Financial Analysis:\\n\")\n",
    "    file.write(f\"-----------------------------------\\n\")\n",
    "    file.write(f\"Total Months: {months}\\n\")\n",
    "    file.write(f\"Total : {npl} USD\\n\")\n",
    "    file.write(f\"Average Change : ${average_monthly_change} USD\\n\")\n",
    "    file.write(f\"Greatest Increase in Profits: {best_increase_month} (${best_increase} USD \\n\")\n",
    "    file.write(f\"Worst Decrease in Profits {worst_decrease_month} (${worst_decrease} USD\")\n",
    "                                                                             \n",
    "    file.close()\n",
    "\n",
    "\n",
    "    "
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}

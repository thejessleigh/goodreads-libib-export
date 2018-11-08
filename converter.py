import csv
import re
import sys


#Abandoned, Not Begun, In Progress, Completed
EXCLUSIVE_SHELF_TO_STATUS = {
	'read': 'Completed',
	'currently-reading': 'In Progress',
	'dnf': 'Abandoned',
	'abandoned': 'Abandoned',
	'to-read': 'Not Begun',
	'tbr': 'Not Begun',
	'own-havent-read': 'Not Begun',
	'owned-unread': 'Not Begun'
}


def convert_csv(args):
	# if args[1] == 'help' or args[1] == '--help':
	# 	print 'your first argument should be the shelf you wish to export to libib from goodreads'
	# 	return
	rows = []

	with open('goodreads_export.csv', 'r') as f:
		reader = csv.DictReader(f)
		rows = [x for x in reader]

	books = [book for book in rows]
	print(books[1])

	libib_keys = ['Added Date',	'Authors', 'Began Date', 'Completed Date', 'Copies', 'Description',	'Group', 'ISBN 10',	'ISBN 13', 'UPC', 'EAN', 'Notes', 'Rating', 'Review', 'Review Date', 'Status', 'Tags',	'Title']
	print(len(libib_keys))

	print('export contains {} books. Writing to \'libib_export.csv\' output file.'.format(len(books)))

	with open('libib_export.csv', 'w') as f:
		writer = csv.writer(f)
		writer.writerow(libib_keys)
		for book in books:
			# Fields left blank are not available in the goodreads export
			row = []
			row.append(re.sub('/', '-',book.get('Date Added', '')))
			authors = [book.get('Author', '')]
			authors.append(book.get('Additional Authors', ''))
			row.append(','.join(authors))
			row.append('') # Began date
			row.append(re.sub('/', '-', book.get('Date Read', '')))
			row.append(book.get('Owned Copies', ''))
			row.append('') # description
			row.append('') # group
			row.append(book.get('ISBN', ''))
			row.append(book.get('ISBN13', ''))
			row.append('') # UPC
			row.append('') # EAN
			row.append(book.get('Private Notes', ''))
			row.append(book.get('My Rating', ''))
			row.append(book.get('My Review', ''))
			row.append('') # Review Date
			exclusive_shelf = book.get('Exclusive Shelf')
			row.append(EXCLUSIVE_SHELF_TO_STATUS[exclusive_shelf]) #status
			tags = [book.get('Bookshelves')]
			row.append(','.join(tags)) #tags
			row.append(book.get('Title', '')) #title

			writer.writerow(row)


convert_csv(sys.argv)

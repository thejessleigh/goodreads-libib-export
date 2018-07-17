import csv
import sys


def convert_csv(args):
	if args[1] == 'help' or args[1] == '--help':
		print 'your first argument should be the shelf you wish to export to libib from goodreads'
		return

	rows = []

	with open('goodreads_export.csv', 'r') as f:
		reader = csv.DictReader(f)
		rows = [x for x in reader]

	shelf = args[1]
	books = [book for book in rows if book['Exclusive Shelf'] == shelf]
	print books[1]

	libib_keys = ['Added Date',	'Authors', 'Began Date', 'Completed Date', 'Copies', 'Description',	'Group', 'ISBN 10',	'ISBN 13', 'UPC', 'EAN', 'Notes', 'Rating', 'Review', 'Review Date', 'Status', 'Tags',	'Title']
	print len(libib_keys)

	print 'shelf {} contains {} books. Writing to \'libib_export.csv\' output file.'.format(args[1], len(books))

	with open('libib_export.csv', 'wb') as f:
		#TODO: Do rest of rows and make sure dates are converted to correct string representation for libib import
		writer = csv.writer(f)
		writer.writerow(libib_keys)
		for book in books:
			row = []
			row.append(book.get('Date Added', ''))
			authors = [book.get('Author', '')]
			authors.append(book.get('Additional Authors', ''))
			row.append(','.join(authors))
			row.append('')
			row.append(book.get('Date Read', ''))
			row.append(book.get('Owned Copies', ''))
			row.append('')
			row.append('')
			row.append('')
			row.append('')
			row.append('')
			row.append('')
			row.append('')
			row.append('')
			row.append('')
			row.append('')
			row.append('')
			writer.writerow(row)


convert_csv(sys.argv)

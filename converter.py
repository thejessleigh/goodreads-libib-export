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
	#print books[1]

	# Keys source: https://support.libib.com/support/import-a-csv-file/#download-csv-import-templates
	# title,creators,description,upc_isbn10,ean_isbn13,group,tags,notes,price,added,publisher,publish_date,length_of,copies,call_number,lexile,ddc,lcc,lccn,oclc,rating,review,review_created,status,began_date,completed_date
	libib_keys = ['title','creators','description','upc_isbn10','ean_isbn13','group','tags','notes','price','added','publisher','publish_date','length_of','copies','call_number','lexile','ddc','lcc','lccn','oclc','rating', 'review','review_created','status','began_date','completed_date']

	print('export contains {} books. Writing to \'libib_export.csv\' output file.'.format(len(books)))

	with open('libib_export.csv', 'w') as f:
		writer = csv.writer(f)
		writer.writerow(libib_keys)
		for book in books:
			# Fields left blank are not available in the goodreads export
			row = []
			row.append(book.get('Title', '')) #title
			# creators
			authors = [book.get('Author', '')]
			authors.append(book.get('Additional Authors', ''))
			row.append(','.join(authors))
			# description
			row.append('') # description
			# upc_isbn10
			row.append(book.get('ISBN', ''))
			# omit - row.append('') # UPC
			# ean_isbn13
			row.append(book.get('ISBN13', ''))
			# omit - row.append('') # EAN
			# group
			row.append('') # group
			# tags
			tags = [book.get('Bookshelves')]
			row.append(','.join(tags)) #tags
			# notes
			row.append(book.get('Private Notes', ''))
			# price
			row.append('') # no data in GoodReads export
			# added
			row.append(re.sub('/', '-',book.get('Date Added', '')))
			# publisher
			row.append(book.get('Publisher', ''))
			# publish_date
			row.append(book.get('Year Published', ''))
			# length_of
			row.append(book.get('Number of Pages', ''))
			# copies
			row.append(book.get('Owned Copies', ''))
			# call_number
			row.append('') # no data in GoodReads export			
			# lexile
			row.append('') # no data in GoodReads export
			# ddc
			row.append('') # no data in GoodReads export
			# lcc
			row.append('') # no data in GoodReads export
			# lccn
			row.append('') # no data in GoodReads export
			# oclc
			row.append('') # no data in GoodReads export
			# rating
			row.append(book.get('My Rating', ''))
			# review
			row.append(book.get('My Review', ''))
			# review_created
			row.append('') # Review Date
			# status
			exclusive_shelf = book.get('Exclusive Shelf')
			row.append(EXCLUSIVE_SHELF_TO_STATUS[exclusive_shelf]) #status
			# began_date
			row.append('') # Began date
			# completed_date
			row.append(re.sub('/', '-', book.get('Date Read', '')))

			writer.writerow(row)

convert_csv(sys.argv)

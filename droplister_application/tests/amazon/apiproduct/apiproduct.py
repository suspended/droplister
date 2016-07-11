from amazonproduct import API
import amazonproduct

config = {
    'access_key': 'AKIAJ7NR4H5C4QHEHOWQ',
    'secret_key': '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',
    'associate_tag': 'carlitossanfe-20',
    'locale': 'us'
}
api = amazonproduct.API(cfg=config)

# get all books from result set and
# print author and title
for book in api.item_search('Books', Publisher='Galileo Press'):
    print '%s: "%s"' % (book.ItemAttributes.Author,
                        book.ItemAttributes.Title)
#!/usr/bin/env python3

import ovh

import sys


def main(domain_name):
	client = ovh.Client()

	access_rules = [
		{'method': 'GET', 'path': '/me'},
		{'method': 'POST', 'path': '/email/domain/{}/redirection'.format(domain_name)},
	]

	validation = client.request_consumerkey(access_rules)

	print("Visit this URL authenticate:", validation['validationUrl'])
	input("and press Enter to continue...\n")

	# Print nice welcome message
	print("Welcome", client.get('/me')['firstname'])
	print("Btw, your 'consumerKey' is '%s'" % validation['consumerKey'])


if __name__ == '__main__':
	domain_name = sys.argv[1]
	main(domain_name)

#!/usr/bin/env python3

import sys

import ovh


def main(domain_name, from_addr, to_addr):
	client = ovh.Client()

	# Create a new alias
	client.post( '/email/domain/{}/redirection'.format(domain_name),
		_from     = from_addr,
		to        = to_addr,
		localCopy = False
	)

	print("Installed new mail redirection: {} --> {}".format(from_addr, to_addr))


if __name__ == '__main__':
	domain_name, from_addr, to_addr = sys.argv[1:]
	main(domain_name, from_addr, to_addr)

lists = [(1, 'A'), (2, 'B'), (3, 'C')]
	#University.query.filter_by(uni_name=University.uni_name).all()
	names = []
	print(lists)
	for i in range(int(len(lists))):
		temp = [lists[i], lists[i]]
		#.uni_name, lists[i].uni_name]'''
		names.append(temp)

	university_name = SelectField("University",
		choices=names)
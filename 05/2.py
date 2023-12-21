
class Rng:
	INDEX=0

	def __init__(self,name,start,length=None,stop=None,offset=None,offset_name=None):
		self.name=name
		self.start=start
		self.length=length
		if stop is not None:
			self.length=stop-self.start

		self.offset=offset
		self.offset_name=offset_name
		self.pr_offs=True
		if self.length is None:
			raise Exception(f"length can not be None. {name} {start} {stop} {offset} {offset_name}")

	def __repr__(self):
		return str(self)

	def rng_str(self):
		return f"{self.start}~{self.length}"

	def __str__(self):
		# if self.pr_offs and self.offset is not None:
		# if self.pr_offs:
		offs=0 if self.offset is None else self.offset
		return f" {self.start:12}~{str(self.length).ljust(12)} {offs:+13d}   {str(self.offset_name).ljust(20)} {self.name}"
		# else:

	def apply_offset(self):
		if self.offset is not None:
			self.start+=self.offset
			self.offset=None
			self.offset_name=None

	def stop(self):
		return self.start+self.length
	def last(self):
		return self.start+self.length-1

	# def __contains__(self,val):
	# 	return self.start<=val<self.start+self.length:

	# def is_strict_inside(self,val):
	# 	return self.start<=val<self.start+self.length:
	def from_str(text):
		Rng.INDEX+=1
		return Rng(f"g{Rng.INDEX}",*[int(x) for x in text.split("~")])

	def split_by(self,rule):
		res=[None]*3
		s_stop=self.stop()
		o_stop=rule.stop()
		if s_stop<=rule.start or self.start>=o_stop:
			res[1]=self
			# print(f"-----  NO HIT: rng \"{self.name}\" ({self.rng_str()}), old rule:\"{self.offset_name}\" \"{rule.name}\".")
			return None
		else:
			if self.offset is not None:
				raise Exception(f"COLLISION: rng \"{self.name}\" ({self.rng_str()}) was generated by rule \"{self.offset_name}\" and is again targeted by \"{rule.name}\".")
			if self.start<rule.start:
				res[0]=Rng(f"{self.name}a",self.start,stop=rule.start)
			if s_stop>o_stop:
				res[2]=Rng(f"{self.name}c",o_stop,stop=s_stop)
			res[1]=Rng(f"{self.name}b",max(self.start,rule.start),stop=min(s_stop,o_stop),offset=rule.offset,offset_name=rule.name)

		return [x for x in res if x is not None]

# class LList:
	# def __init__(self):
		# self.head=None
	# def add

# class Element:
# 	def __init__(self,value):
# 		self.prev=None
# 		self.next=None
# 		self.value=value

def main():

	if TEST(False):
	# if TEST(True):
		return
	print("\n\n\n\n")
	print("#############")
	print("## New run ##")
	print("#############")
	print("\n")

	if True:
		with open("input") as f:
		# with open("input-small") as f:
			inp=f.read()

		paras=inp.split("\n\n")

		seeds=[int(x) for x in paras[0].split(": ")[1].split(" ")]
		rngs=[Rng(str((i//2)+1),seeds[i],seeds[i+1]) for i in range(0,len(seeds),2)]

		# for rng in rngs:
			# print(rng)

		# print(len(seeds))
		# return

		order=[
			"seed",
			"soil",
			"fertilizer",
			"water",
			"light",
			"temperature",
			"humidity",
		]

		header_rules={}

		for pidx,para in enumerate(paras[1:]):
			lines=para.split("\n")
			header=lines[0].split("-")[0]
			header_rules[header]=[]
			for lidx,line in enumerate(lines[1:]):
				arr=[int(x) for x in line.split(" ")]
				rule=Rng(f"{header}:{pidx+1}.{lidx+1}",arr[1],arr[2],offset=arr[0]-arr[1])
				header_rules[header].append(rule)

		# for h,rs in rules.items():
		# 	print(f"- {h}")
		# 	for r in rs:
		# 		print(f" - {r}")

	# rngs=[
	# 	Rng("1",0,10)
	# ]

	# rules=[
	# 	Rng("r1",1,2,offset=10),
	# 	Rng("r2",5,2,offset=100),
	# 	Rng("r3",8,1,offset=1000),
	# ]

	# llist_head=Element(rngs[0])
	# llist_curr=llist_head
	# for rng in rngs[1:]:
	# 	element=Element(rng)
	# 	llist_curr.next=element
	# 	element.prev=llist_curr
	# 	llist_curr=llist_curr.next


	# print_llist(llist_curr)
	# return


	# for rng in rngs:
	# 	rng.length=1
		# print(f"  {rng}")
	# for header,rules in header_rules.items():
	for header in order:
		rules=header_rules[header]
		for rule in rules:
			print(f"RULE {rule.name}")
			contin=True
			index=0
			while index<len(rngs):
				curr=rngs[index]
				elems=curr.split_by(rule)
				if elems is None:
					index+=1
				else:
					for eidx,elem in enumerate(elems):
						rngs.insert(index+eidx,elem)
					index+=len(elems)
					rngs.pop(index)

					# print(f" new at {index-len(elems)}-{index}:")
					# for rng in rngs:
					# 	print(f"  {rng}")
		for rng in rngs:
			rng.apply_offset()

		# print("\n WITH OFFSET")
		# for rng in rngs:
		# 	rng.apply_offset()
		# 	print(f"  {rng}")
		# 	# print_llist()

	min_locs=sorted([rng.start for rng in rngs])
	for loc in min_locs:
		print(loc)

		# break
	# new_rngs=[]
	# for rng in rngs:
	# 	temp_rngs=[rng]
	# 	for rule in rules:
	# 		temp_rngs=

	# for

# def print_llist(llist):
# 	if llist is not None:
# 		# print(f"llist 0: {llist.value}")
# 		index=0
# 		contin=True
# 		while contin:
# 			print(f"llist {index}: {llist.value}")
# 			contin=llist.next is not None
# 			if contin:
# 				llist=llist.next
# 				index+=1


def TEST(test):
	if  test:
		test_rng()

	return test

def test_rng():
	cases=[
		["3~4","1~2",            "3~4"],
		["3~4","1~3",      "3~1","4~3"],
		["3~4","1~4",      "3~2","5~2"],
		["3~4","1~5",      "3~3","6~1"],
		["3~4","1~6",      "3~4"      ],
		["3~4","3~4",      "3~4"      ],
		["3~4","3~3",      "3~3","6~1"],
		["3~4","1~7",      "3~4"      ],
		["3~4","1~8",      "3~4"      ],
		["3~4","2~8",      "3~4"      ],
		["3~4","3~8",      "3~4"      ],
		["3~4","4~8","3~1","4~3"      ],
		["3~4","5~8","3~2","5~2"      ],
		["3~4","6~8","3~3","6~1"      ],
		["3~4","7~8","3~4"            ],
		["3~4","4~2","3~1","4~2","6~1"],
	]
	for idx,case in enumerate(cases):

		rng=Rng.from_str(case[0])
		rule=Rng.from_str(case[1])

		# print(f"{idx+1=},{rng=},{rule=}")

		res=rng.split_by(rule)

		res=[str(x) for x in res]

		success=True
		for a,b in zip(case[2:],res):
			if a!=b:
				success=False
		if not success:
			print(f" case {idx+1}/{len(cases)} ({case}) failed, result: {res}")
		# else:
		# 	print(f" case {idx+1}/{len(cases)} ({case}) succeeded, result: {res}")


main()

Here is the basic structure of classes for each question.
For q1 in q1.py, there is one class named "Flower".
	There are 3 data fields:
		name(a string):The name of this flower
		numOfPet(an int):The number of petals
		price(a float):The price of this flower
	There are 9 methods:
		__init__():Initialize datafields
		getName():No input|Output a string
			return the name of instance
			*if there is no name, print a error message.
		getNumOfPet():No input|Output an int
			return the number of petals of instance
			*if there is no numOfPet, print a error message.
		getNumOfPet():No input|Output an float
			return the price of instance
			*if there is no price, print a error message.
		getValue():No input|Output a dict
			output a dict of values
		setName(str):1 input|No output
			set name
			*if input is not a string, print a error message.
		setNumOfPet(int):1 input|No output
			set numOfPet
			*if input is not an integer, print a error message.
		setPrice(float):1 input|No output
			set price
			*if input is not a number, print a error message.
			*if input number has more than 2 digit in the fractional part, print a error message.
		setValue(str,int,float):3 input|No output
			set name,numOfPet,price
			*Only first type error will be reported

For q2 in q2.py, there is one class named "Polynomial".
	There are 2 data fields:
		func(a string):The original function to operate
		*The data field above is required to input by user.

		after_derivative(a string):The function after taking derivative
	There are 2 methods:
		__init__():Initialize datafields
		derivative():No input|No output
			Only called in initializer, automatically take the derivative of the original function.

For q3 in q3.py, there is one class named "ecosystem".
	There are 6 data fields:
		riverLen(an int):The length of river
		numOfBear(an int):The number of bears
		numOfFish(an int):The number of fishes
		*The data field above is required to input by user.

		numOfAnimal(an int):The number of animal existing
			Used to check if river is full
		newlyCreated(a list):Storing the index of newly borned animals
			The animals in this list should not be operated in this iteration
		river(a list):Storing the status of each space in the ecosystem
			The variable that most operation is done

	There are 6 methods:
		__init__():Initialize datafields
		__str__():Output the state of river by a sequence of 'N','B', and 'F'
		addAnimal(int,str):2 inputs|No output
			Randomly assign a few number of some kind of animals into empty spaces.
			*If the animals to be add is more than empty spaces, do nothing.
		bearBehaviour(int):1 input|No output
			If target position is empty, go there.
			If target position is a bear, add 1 bear.
			If target position is a fish, overwrite it.
		fishBehaviour(int):1 input|No output
			If target position is empty, go there.
			If target position is a bear, disappear.
			If target position is a fish, add 1 fish.
		simulate(int):1 input|No output
			Do a few rounds of simulations, operate movement in the list one by one in one simulation.
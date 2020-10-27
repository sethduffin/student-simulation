from random import choice
from time import sleep
import os

class color:
    blue = '\033[94m'
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    stop = '\033[0m'
    bold = '\033[1m'
    underline = '\033[4m'

first_names = "Liam Noah William James Logan Benjamin Mason Elijah Oliver Jacob Lucas Michael Alexander Ethan Daniel Matthew Aiden Henry Joseph Jackson Samuel Sebastian David Carter Wyatt Jayden John Owen Dylan Luke Gabriel Anthony Isaac Grayson Jack Julian Levi Christopher Joshua Andrew Lincoln Mateo Ryan Jaxon Nathan Aaron Isaiah Thomas Charles Caleb Josiah Christian Hunter Eli Jonathan Connor Landon Adrian Asher Cameron Leo Theodore Jeremiah Hudson Robert Easton Nolan Nicholas Ezra Colton Angel Brayden Jordan Dominic Austin Ian Adam Elias Jaxson Greyson Jose Ezekiel Carson Evan Maverick Bryson Jace Cooper Xavier Parker Roman Jason Santiago Chase Sawyer Gavin Leonardo Kayden Ayden Jameson Kevin Bentley Zachary Everett Axel Tyler Micah Vincent Weston Miles Wesley Nathaniel Harrison Brandon Cole Declan Luis Braxton Damian Silas Tristan Ryder Bennett George Emmett Justin Kai Max Diego Luca Ryker Carlos Maxwell Kingston Ivan Maddox Juan Ashton Jayce Rowan Kaiden Giovanni Eric Jesus Calvin Abel King Camden Amir Blake Alex Brody Malachi Emmanuel Jonah Beau Jude Antonio Alan Elliott Elliot Waylon Xander Timothy Victor Bryce Finn Brantley Edward Abraham Patrick Grant Karter Hayden Richard Miguel Joel Gael Tucker Rhett Avery Steven Graham Kaleb Jasper Jesse Matteo Dean Zayden Preston August Oscar Jeremy Alejandro Marcus Dawson Lorenzo Messiah Zion Maximus Related Post River Zane Mark Brooks Nicolas Paxton Judah Emiliano Kaden Bryan Kyle Myles Peter Charlie Kyrie Thiago Brian Kenneth Andres Lukas Aidan Jax Caden Milo Paul Beckett Brady Colin Omar Bradley Javier Knox Jaden Barrett Israel Matias Jorge Zander Derek Josue Cayden Holden Griffin Arthur Leon Felix Remington Jake Killian Clayton Sean Adriel Riley Archer Legend Erick Enzo Corbin Francisco Dallas Emilio Gunner Simon Andre Walter Damien Chance Phoenix Colt Tanner Stephen Kameron Tobias Manuel Amari Emerson Louis Cody Finley Iker Martin Rafael Nash Beckham Cash Karson Rylan Reid Theo Ace Eduardo Spencer Raymond Maximiliano Anderson Ronan Lane Cristian Titus Travis Jett Ricardo Bodhi Gideon Jaiden Fernando Mario Conor Keegan Ali Cesar Ellis Jayceon Walker Cohen Arlo Hector Dante Kyler Garrett Donovan Seth Jeffrey Tyson Jase Desmond Caiden Gage Atlas Major Devin Edwin Angelo Orion Conner Julius Marco Jensen Daxton Peyton Zayn Collin Jaylen Dakota Prince Johnny Kayson Cruz Hendrix Atticus Troy Kane Edgar Sergio Kash Marshall Johnathan Romeo Shane Warren Joaquin Wade Leonel Trevor Dominick Muhammad Erik Odin Quinn Jaxton Dalton Nehemiah Frank Grady Gregory Andy Solomon Malik Rory Clark Reed Harvey Zayne Jay Jared Noel Shawn Fabian Ibrahim Adonis Ismael Pedro Leland Malakai Malcolm Alexis Kason Porter Emma Olivia Ava Isabella Sophia Mia Charlotte Amelia Evelyn Abigail Harper Emily Elizabeth Avery Sofia Ella Madison Scarlett Victoria Aria Grace Chloe Camila Penelope Riley Layla Lillian Nora Zoey Mila Aubrey Hannah Lily Addison Eleanor Natalie Luna Savannah Brooklyn Leah Zoe Stella Hazel Ellie Paisley Audrey Skylar Violet Claire Bella Aurora Lucy Anna Samantha Caroline Genesis Aaliyah Kennedy Kinsley Allison Maya Sarah Madelyn Adeline Alexa Ariana Elena Gabriella Naomi Alice Sadie Hailey Eva Emilia Autumn Quinn Nevaeh Piper Ruby Serenity Willow Everly Cora Kaylee Lydia Aubree Arianna Eliana Peyton Melanie Gianna Isabelle Julia Valentina Nova Clara Vivian Reagan Mackenzie Madeline Brielle Delilah Isla Rylee Katherine Sophie Josephine Ivy Liliana Jade Maria Taylor Hadley Kylie Emery Adalynn Natalia Annabelle Faith Alexandra Ximena Ashley Brianna Raelynn Bailey Mary Athena Andrea Leilani Jasmine Lyla Margaret Alyssa Adalyn Arya Norah Khloe Kayla Eden Eliza Rose Ariel Melody Alexis Isabel Sydney Juliana Lauren Iris Emerson London Morgan Lilly Charlie Aliyah Valeria Arabella Sara Finley Trinity Ryleigh Jordyn Jocelyn Kimberly Esther Molly Valerie Cecilia Anastasia Daisy Reese Laila Mya Amy Teagan Amaya Elise Harmony Paige Adaline Fiona Alaina Nicole Genevieve Lucia Alina Mckenzie Callie Payton Eloise Brooke Londyn Mariah Julianna Rachel Daniela Gracie Catherine Angelina Presley Josie Harley Adelyn Vanessa Makayla Parker Juliette Amara Marley Lila Ana Rowan Alana Michelle Malia Rebecca Brooklynn Brynlee Summer Sloane Leila Sienna Adriana Sawyer Kendall Juliet Destiny Alayna Elliana Diana Hayden Ayla Dakota Angela Noelle Rosalie Joanna Jayla Alivia Lola Emersyn Georgia Selena June Daleyza Tessa Maggie Jessica Remi Delaney Camille Vivienne Hope Mckenna Gemma Olive Alexandria Blakely Izabella Catalina Raegan Journee Gabrielle Lucille Ruth Amiyah Evangeline Blake Thea Amina Giselle Lilah Melissa River Kate Adelaide Charlee Vera Leia Gabriela Zara Jane Journey Elaina Miriam Briella Stephanie Cali Ember Lilliana Aniyah Logan Kamila Brynn Ariella Makenzie Annie Mariana Kali Haven Elsie Nyla Paris Lena Freya Adelynn Lyric Camilla Sage Jennifer Paislee Talia Alessandra Juniper Fatima Raelyn Amira Arielle Phoebe Kinley Ada Nina Ariah Samara Myla Brinley Cassidy Maci Aspen Allie Keira Kaia Makenna Amanda Heaven Joy Lia Madilyn Gracelyn Laura Evelynn Lexi Haley Miranda Kaitlyn Daniella Felicity Jacqueline Evie Angel Danielle Ainsley Dylan Kiara Millie Jordan Maddison Rylie Alicia Maeve Margot Kylee Phoenix Heidi Zuri Alondra Lana Madeleine Gracelynn Kenzie Miracle Shelby Elle Adrianna Bianca Addilyn Kira Veronica Gwendolyn Esmeralda Chelsea Alison Skyler Magnolia Daphne Jenna Everleigh Kyla Braelynn Harlow Annalise Mikayla Dahlia Maliyah Averie Scarlet Kayleigh Luciana Kelsey Nadia".split(" ")
last_names = "Smith Johnson Williams Jones Brown Davis Miller Wilson Moore Taylor Anderson Thomas Jackson White Harris Martin Thompson Garcia Martinez Robinson Clark Rodriguez Lewis Lee Walker Hall Allen Young Hernandez King Wright Lopez Hill Scott Green Adams Baker Gonzalez Nelson Carter Mitchell Perez Roberts Turner Phillips Campbell Parker Evans Edwards Collins Stewart Sanchez Morris Rogers Reed Cook Morgan Bell Murphy Bailey Rivera Cooper Richardson Cox Howard Ward Torres Peterson Gray Ramirez James Watson Brooks Kelly Sanders Price Bennett Wood Barnes Ross Henderson Coleman Jenkins Perry Powell Long Patterson Hughes Flores Washington Butler Simmons Foster Gonzales Bryant Alexander Russell Griffin Diaz Hayes Myers Ford Hamilton Graham Sullivan Wallace Woods Cole West Jordan Owens Reynolds Fisher Ellis Harrison Gibson Mcdonald Cruz Marshall Ortiz Gomez Murray Freeman Wells Webb Simpson Stevens Tucker Porter Hunter Hicks Crawford Henry Boyd Mason Morales Kennedy Warren Dixon Ramos Reyes Burns Gordon Shaw Holmes Rice Robertson Hunt Black Daniels Palmer Mills Nichols Grant Knight Ferguson Rose Stone Hawkins Dunn Perkins Hudson Spencer Gardner Stephens Payne Pierce Berry Matthews Arnold Wagner Willis Ray Watkins Olson Carroll Duncan Snyder Hart Cunningham Bradley Lane Andrews Ruiz Harper Fox Riley Armstrong Carpenter Weaver Greene Lawrence Elliott Chavez Sims Austin Peters Kelley Franklin Lawson Fields Gutierrez Ryan Schmidt Carr Vasquez Castillo Wheeler Chapman Oliver Montgomery Richards Williamson Johnston Banks Meyer Bishop Mccoy Howell Alvarez Morrison Hansen Fernandez Garza Harvey Little Burton Stanley Nguyen George Jacobs Reid Kim Fuller Lynch Dean Gilbert Garrett Romero Welch Larson Frazier Burke Hanson Day Mendoza Moreno Bowman Medina Fowler Brewer Hoffman Carlson Silva Pearson Holland Douglas Fleming Jensen Vargas Byrd Davidson Hopkins May Terry Herrera Wade Soto Walters Curtis Neal Caldwell Lowe Jennings Barnett Graves Jimenez Horton Shelton Barrett Obrien Castro Sutton Gregory Mckinney Lucas Miles Craig Rodriquez Chambers Holt Lambert Fletcher Watts Bates Hale Rhodes Pena Beck Newman Haynes Mcdaniel Mendez Bush Vaughn Parks Dawson Santiago Norris Hardy Love Steele Curry Powers Schultz Barker Guzman Page Munoz Ball Keller Chandler Weber Leonard Walsh Lyons Ramsey Wolfe Schneider Mullins Benson Sharp Bowen Daniel Barber Cummings Hines Baldwin Griffith Valdez Hubbard Salazar Reeves Warner Stevenson Burgess Santos Tate Cross Garner Mann Mack Moss Thornton Dennis Mcgee Farmer Delgado Aguilar Vega Glover Manning Cohen Harmon Rodgers Robbins Newton Todd Blair Higgins Ingram Reese Cannon Strickland Townsend Potter Goodwin Walton Rowe Hampton Ortega Patton Swanson Joseph Francis Goodman Maldonado Yates Becker Erickson Hodges Rios Conner Adkins Webster Norman Malone Hammond Flowers Cobb Moody Quinn Blake Maxwell Pope Floyd Osborne Paul Mccarthy Guerrero Lindsey Estrada Sandoval Gibbs Tyler Gross Fitzgerald Stokes Doyle Sherman Saunders Wise Colon Gill Alvarado Greer Padilla Simon Waters Nunez Ballard Schwartz Mcbride Houston Christensen Klein Pratt Briggs Parsons Mclaughlin Zimmerman French Buchanan Moran Copeland Roy Pittman Brady Mccormick Holloway Brock Poole Frank Logan Owen Bass Marsh Drake Wong Jefferson Park Morton Abbott Sparks Patrick Norton Huff Clayton Massey Lloyd Figueroa Carson Bowers Roberson Barton Tran Lamb Harrington Casey Boone Cortez Clarke Mathis Singleton Wilkins Cain Bryan Underwood Hogan Mckenzie Collier Luna Phelps Mcguire Allison Bridges Wilkerson Nash Summers Atkins Wilcox Pitts Conley Marquez Burnett Richard Cochran Chase Davenport Hood Gates Clay Ayala Sawyer Roman Vazquez Dickerson Hodge Acosta Flynn Espinoza Nicholson Monroe Wolf Morrow Kirk Randall Anthony Whitaker Oconnor Skinner Ware Molina Kirby Huffman Bradford Charles Gilmore Dominguez Oneal Bruce Lang Combs Kramer Heath Hancock Gallagher Gaines Shaffer Short Wiggins Mathews Mcclain Fischer Wall Small Melton Hensley Bond Dyer Cameron Grimes Contreras Christian Wyatt Baxter Snow Mosley Shepherd Larsen Hoover Beasley Glenn Petersen Whitehead Meyers Keith Garrison Vincent Shields Horn Savage Olsen Schroeder Hartman Woodard Mueller Kemp Deleon Booth Patel Calhoun Wiley Eaton Cline Navarro Harrell Lester Humphrey Parrish Duran Hutchinson Hess Dorsey Bullock Robles Beard Dalton Avila Vance Rich Blackwell York Johns Blankenship Trevino Salinas Campos Pruitt Moses Callahan Golden Montoya Hardin Guerra Mcdowell Carey Stafford Gallegos Henson Wilkinson Booker Merritt Miranda Atkinson Orr Decker Hobbs Preston Tanner Knox Pacheco Stephenson Glass Rojas Serrano Marks Hickman English Sweeney Strong Prince Mcclure Conway Walter Roth Maynard Farrell Lowery Hurst Nixon Weiss Trujillo Ellison Sloan Juarez Winters Mclean Randolph Leon Boyer Villarreal Mccall Gentry Carrillo Kent Ayers Lara Shannon Sexton Pace Hull Leblanc Browning Velasquez Leach Chang House Sellers Herring Noble Foley Bartlett Mercado Landry Durham Walls Barr Mckee Bauer Rivers Everett Bradshaw Pugh Velez Rush Estes Dodson Morse Sheppard Weeks Camacho Bean Barron Livingston Middleton Spears Branch Blevins Chen Kerr Mcconnell Hatfield Harding Ashley Solis Herman Frost Giles Blackburn William Pennington Woodward Finley Mcintosh Koch Best Solomon Mccullough Dudley Nolan Blanchard Rivas Brennan Mejia Kane Benton Joyce Buckley Haley Valentine Maddox Russo Mcknight Buck Moon Mcmillan Crosby Berg Dotson Mays Roach Church Chan Richmond Meadows Faulkner Oneill Knapp Kline Barry Ochoa Jacobson Gay Avery Hendricks Horne Shepard Hebert Cherry Cardenas Mcintyre Whitney Waller Holman Donaldson Cantu Terrell Morin Gillespie Fuentes Tillman Sanford Bentley Peck Key Salas Rollins Gamble Dickson".split(" ")

def get_name():
	return choice(first_names)+' '+choice(last_names)

def load_saved():
	from cache import saved
	saves =	list(filter(lambda x: not x.startswith('__') and x != 'TEMPLATE', dir(saved)))
	if len(saves) > 0:
		print()
		os.system('clear')
		print('You have saved information. Load a save or fill out new info.')
		print('  0. NEW INFO')
		for i,key in enumerate(saves):
			print('  %s. %s' % (i+1,key))
		try:
			choice = int(input(color.yellow+"Choice: "+color.stop))
		except:
			quit()
		ret = None
		if choice == 0:
			ret = saved.TEMPLATE
		elif choice > 0 and choice <= len(saves):
			ret = eval('saved.'+saves[choice-1])
		else:
			print(color.red+'No option for the choice: '+str(choice)+color.stop)
			sleep(1)
			ret = load_saved()
		print()
		return ret
	else:
		return saved.TEMPLATE

def save_info(info):
	name = info.students.username
	save = '''
	class %s:
		course_count = %s
		courses = %s
		class admin:
			username = "%s"
			password = "%s"
			email = "%s"
		class students:
			username = "%s"
			password = "%s"
			ammount = %s
			keys = %s''' % (name,
		info.course_count,
		info.courses,
		info.admin.username,
		info.admin.password,
		info.admin.email,
		info.students.username,
		info.students.password,
		info.students.ammount,
		info.students.keys,)

	with open('cache.py','a') as file:
		file.write(save)
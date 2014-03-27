import praw
from commonregex import CommonRegex




class redditBot(object):
r = praw.Reddit("Annotation_Bot by /u/jbaham")
	
	def __init__(self, r):
		self.r = r

	def userLogin(self):
		self.r.login("username", "password")

	#Targets either specific post or the top given number of posts from hot category
	def getPosts(self):
		#sub = r.get_subreddit('askhistorians').get_hot(limit=2) #uncomment to get the top posts of a certain subreddit
		sub = r.get_submission(submission_id='217yxs') #this allows the user to select a particular submission
		return sub

	#Collects the comments in the subreddit
	def getComments(self):
		submission = self.getPosts()
		print submission
		#for sub in submission:  
		forest_comments = praw.helpers.flatten_tree(submission.comments)
		for comment in forest_comments:
			my_Reply =  self.getLinks(comment.body)
			try:
				comment.reply(my_Reply)
			except:
				pass
			

	#takes the comment.body text and scrapes the urls. 
	def getLinks(self, comment):
		parsed_text = CommonRegex(comment)
		links = []
		for link in parsed_text.links:
	 		links.append(link) 
	 	return self.makeReply(links) 
	 	
	#take the list of links and format properly for the reddit reply		
	def makeReply(self, links): 
		reply = ''
		i = 1
		for item in links:
			reply += ''.join(str(i) + "." + " " + "[" + item + "]" + "(" + item + ")" + "\n") 
			i += 1
		return reply 



bot = redditBot(r)
bot.userLogin()
#bot.getPosts()
#bot.getLinks()
bot.getComments()




	







import twitter

api = twitter.Api(consumer_key='consumer_key_here',
                  consumer_secret='consumer_secret_here',
                  access_token_key='access_token_key_here',
                  access_token_secret='access_token_secret_here')


l = ['sinanata','workremoteus'] #list of twitter handles you would like to add to your list
batch_size = 99

for i in range(0, len(l), batch_size):
    api.CreateListsMember(list_id=your_list_id_here, screen_name=l[i:i+batch_size])

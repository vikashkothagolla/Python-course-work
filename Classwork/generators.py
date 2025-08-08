'''def stream_music(tracks):
    for i in tracks:
        yield i
playlist = stream_music(["chunk", "chunk", "chunk"])
print(next(playlist)) # Output: Song1'''

'''def simple_generator():
    print("Start")
    yield 1
    yield 2
    yield 3
    print("End")
# Create a generator object
gen = simple_generator()
print(next(gen)) 
print(next(gen)) 
print(next(gen))'''

'''def square_numbers(n):
 for i in range(n):
  yield i * i
squares = square_numbers(5)
print(next(squares)) # Output: 0
print(next(squares)) # Output: 1
print(next(squares)) 
print(next(squares)) 
print(next(squares)) '''

'''def power(n):
    for i in range(1,n):
        yield i*10
power=power(100)
print(next(power))
print(next(power))
print(next(power))
print(next(power))
print(next(power))
print(next(power))'''

#upto n like 1 2 3 4 5
'''def countn(n):
    count=1
    while count<=n:
        yield count
        count+=1
countnn=countn(90)
print(next(countnn))
print(next(countnn))        
print(next(countnn))
print(next(countnn))
print(next(countnn))'''

#upto n but reverse
'''def countn(n):
    while n>0:
        yield n
        n-=1
countnn=countn(9)
print(next(countnn))
print(next(countnn))        
print(next(countnn))
print(next(countnn))
print(next(countnn))'''
#video_stream 
'''def stream_video(chunks):
    for chunk in chunks:
        yield chunk
video_chunk=("chh1","ch1","ch3")
player=stream_video(video_chunk) 
print(next(player))
print(next(player))
print(next(player))'''

#auido_stream
def stream_auido(tracks):
    for track in tracks:
        yield track
audio_track=("auido1","auido2","auido3")
player=stream_auido(audio_track)
print(next(player)) 
print(next(player))     
print(next(player))            

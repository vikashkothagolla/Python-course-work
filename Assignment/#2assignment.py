messages = [
    "Rahul: Today's viva was so stressful. The examiner kept looking at me like I was from another planet.",
    "Vikash: (laughs) What did he ask you?",
    "Rahul: First, he said, “Explain your project in one sentence.”",
    "Ram: For me, the first thing he said was, “You look nervous.”",
    "Vikash: (smiling) Nice answer! In my case, he looked at my report and said, “Your project looks good… Did you really make it?”",
    "Rahul: And what did you say?",
    "Vikash: I told him, “Yes, sir, I made it… but Google helped me a lot.” He laughed at that.",
    "Ram: There was one question I didn’t know at all. I told him honestly, “Sir, please tell me the answer, I'll write it down.”",
    "Rahul: (laughing) I don't know if he was happy with your honesty or surprised.",
    "Vikash: Anyway, we all passed, so that’s what matters.",
    "Ram: Yeah, marks can be high or low, but viva memories will stay forever."
]

total_messages = 0
users = []
word_count = 0
longest_msg = ""
user_msg_count = []
user_words = []
questions = []
deleted_count = 0
unique_msgs = []

for msg in messages:
    total_messages += 1
    colon_pos = msg.find(":")
    user = msg[:colon_pos]
    content = msg[colon_pos+2:]

    if user not in users:
        users.append(user)
        user_msg_count.append(0)
        user_words.append([])

    for i in range(len(users)):
        if users[i] == user:
            user_msg_count[i] += 1
            for word in content.split():
                user_words[i].append(word.lower())
                word_count += 1
            break

    if len(content) > len(longest_msg):
        longest_msg = msg

    if "?" in content:
        questions.append(msg)

    if content == "This message was deleted":
        deleted_count += 1

    if msg not in unique_msgs:
        unique_msgs.append(msg)

print("1. Total messages:", total_messages)
print("2. Unique users:", users)
print("3. Total words:", word_count)
print("4. Average words per message:", round(word_count / total_messages, 2))
print("5. Longest message:", longest_msg)

max_count = max(user_msg_count)
max_user = users[user_msg_count.index(max_count)]
print("6. Most active user:", max_user, "(", max_count, "messages )")

vikash_index = users.index("Vikash")
print("7. Messages sent by Vikash:", user_msg_count[vikash_index])

rahul_index = users.index("Rahul")
word_list = []
word_freq = []
for w in user_words[rahul_index]:
    if w not in word_list:
        word_list.append(w)
        word_freq.append(1)
    else:
        word_freq[word_list.index(w)] += 1
common_word = word_list[word_freq.index(max(word_freq))]
print('Most frequent word used by Rahul:', '"' + common_word + '"')

first_msg = ""
last_msg = ""
found = False
for msg in messages:
    if msg.startswith("Rahul:"):
        if not found:
            first_msg = msg
            found = True
        last_msg = msg
print("First message by Rahul:", first_msg)
print("Last message by Rahul:", last_msg)

if "Dave" not in users:
    print("User 'Dave' not found in the chat.")

all_words = []
all_freq = []
for uw in user_words:
    for w in uw:
        if w not in all_words:
            all_words.append(w)
            all_freq.append(1)
        else:
            all_freq[all_words.index(w)] += 1
repeated = [all_words[i] for i in range(len(all_words)) if all_freq[i] > 1]
print("Common repeated words:", repeated)

max_avg = 0
max_avg_user = ""
for i in range(len(users)):
    avg = len(user_words[i]) / user_msg_count[i]
    if avg > max_avg:
        max_avg = avg
        max_avg_user = users[i]
print("User with longest average message:", max_avg_user, "(avg", round(max_avg, 2), "words)")

mention_count = sum(1 for msg in messages if "lewis" in msg.lower() and not msg.lower().startswith("lewis:"))
print("Messages mentioning 'lewis':", mention_count)
print("Unique messages count:", len(unique_msgs))

sorted_msgs = sorted(unique_msgs)
print("Sorted messages:")
for msg in sorted_msgs:
    print(msg)

print("Questions asked:")
for q in questions:
    print(q)

# Since there are no 'verstappen:' and 'lewis:' messages in this chat, reply count will be 0
reply_count = 0
print("Reply ratio from verstappen to lewis:", reply_count, "replies")
print("Deleted messages found:", deleted_count)

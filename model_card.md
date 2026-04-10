# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

I gave my model the name tune ranker because it ranks tunes.

---

## 2. Intended Use  

I designed this recommender to suggest songs based on a user’s preferred genre, mood, and energy level. I built it for classroom exploration, so it assumes simple user preferences and is not meant for real-world production use.

## 3. How the Model Works  

I use features like genre, mood, energy, and acousticness to compare songs with what the user likes. I assign scores based on how closely a song matches those preferences, and I improved the model by adding smoother scoring and more features instead of just exact matches.
---

## 4. Data  

Describe the dataset the model uses.  

My dataset has a small catalog of about 10 songs with different genres and moods like pop, lofi, rock, and jazz. It is limited and does not cover many styles or global music tastes, so it only represents a narrow range of music.

## 5. Strengths  

My system works well for users with clear preferences like happy pop or chill lofi because it can match those features directly. I noticed that the recommendations often matched what I would personally expect for those types of users.  

---

## 6. Limitations and Bias 

My model does not consider things like lyrics, artist popularity, or cultural context, which limits its understanding of music. It can also favor certain genres or moods more heavily depending on the scoring weights, which could make recommendations less fair.

## 7. Evaluation  

I tested my model using different user profiles like high-energy pop and low-energy chill listeners to see if the results made sense. I looked at whether the top songs matched my expectations and was surprised how much small weight changes affected the rankings.

---

## 8. Future Work  

I would improve the model by adding more features like tempo preferences and allowing more complex user profiles. I would also try to increase diversity in recommendations so it does not always suggest very similar songs.

## 9. Personal Reflection  

I learned that recommender systems are really about designing good scoring rules and not just using complex algorithms. This project made me realize how much bias and design choices can influence what users see in apps like Spotify.

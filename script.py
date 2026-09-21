import facebook
token = "আপনার_ফেসবুক_এপিআই_টোকেন_এখানে_বসান"
fb = facebook.GraphAPI(access_token=token)
post_id = "নানা_ভাইয়ের_পোস্ট_আইডি"
comment_text = "একদম লাখ টাকার খাঁটি কথা বলেছেন নানা ভাই। আমরা সবসময় আপনার পাশে আছি।"
fb.put_comment(object_id=post_id, message=comment_text)
print("মাহবুর ভাই, এপিআই সফলভাবে কাজ করেছে!")

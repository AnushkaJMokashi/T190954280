import streamlit as st
import random
from difflib import SequenceMatcher

# Define patterns and responses for the meal ordering chatbot
patterns_responses = {
    "hi": ["Hello! Welcome to our shop. How can I assist you with your meal order today?"],
    "what meals do you offer": ["We offer a variety of meals including veg, nonveg, desserts. What flavor are you interested in?"],
    "what sizes are available": ["Our meals are available in sizes ranging from 6 inches to 12 inches in diameter. What size would you like?"],
    "do you offer delivery": ["Yes, we offer delivery within the city limits. Please provide your address so we can calculate the delivery fee."],
    "how much does a meal cost": ["The cost of our meals depends on the size and flavor. What size and flavor are you interested in?"],
    "how can I place an order": ["You can place an order by calling our hotline at Pune, by visiting our website and using our online order form, or by visiting our shop in person."],
    "do you offer gluten-free options": ["Yes, we offer gluten-free options for some of our meals. Please let us know your dietary restrictions and we can provide more information."],
    "can I customize my meal": ["Yes, we offer custom meal. Please provide details about your desired design and we'll be happy to assist you further."],
    "what are your payment options": ["We accept cash, credit/debit cards, and mobile payment apps. Payment is required upon placing your order."],
    "Cost of Burger":["Cost of Burgers randes from Rs 199 to Rs 300"],
    "Can I order dessert" :["Yes, we have variety of dessert like ice-creams, puddings, cakes,ets"],
    "how long in advance should I order for mass quantity order": ["We recommend placing your order at least 24-48 hours in advance, especially for custom meals. However, we may be able to accommodate rush orders depending on our current schedule."],
    "bye": ["Thank you for considering our shop for your meal purchase! Have a wonderful day!"]
}



# Fallback response for unmatched input
fallback_responses = [
    "I'm sorry, I didn't understand that. How can I assist you with your cake order?",
    "I'm not sure I understand. Can you please rephrase that?"
]

# Sample images for demonstration
veg_images = {
    "Salad":"salad.jpeg",
    "Soup": "soup.jpeg",
    "Vegetable Curry": "curry.jpeg",
}

nonveg_images = {
    "Chicken Wings": "wigs.jpeg",
    "Steak": "steak.jped",
    "Fish Tacos": "fish.jpeg",
}

all_images = {
    "Burger": "burger.jpeg",
    "Pizza": "pizza.jpeg",
    "Sushi": "sushi.jpeg",
}

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

# Function to generate response for the chatbot
def respond(input_text):
    input_text = input_text.lower()
    max_similarity = 0
    best_match_response = None
    
    ## top fine best similar pattern and its responses
    # Threshold for similarity to consider a match
    threshold = 0.5
    
    for pattern, responses in patterns_responses.items():
        similarity = similar(input_text, pattern)
        if similarity > max_similarity and similarity >= threshold:
            max_similarity = similarity
            best_match_response = random.choice(responses)
            
    if best_match_response is None:
        best_match_response = random.choice(fallback_responses)
        
    return best_match_response

# Function to generate response for the chatbot
def respond(input_text):
    input_text = input_text.lower()
    max_similarity = 0
    best_match_response = None
    
    # Threshold for similarity to consider a match
    threshold = 0.5
    
    for pattern, responses in patterns_responses.items():
        similarity = similar(input_text, pattern)
        if similarity > max_similarity and similarity >= threshold:
            max_similarity = similarity
            best_match_response = random.choice(responses)
            
    if best_match_response is None:
        best_match_response = random.choice(fallback_responses)
        
    return best_match_response

# Streamlit app
def main():
    st.title("Food Ordering and Cake Ordering Chatbot")

    st.markdown("""
    ### Food Ordering and Cake Ordering Chatbot
    
    Welcome to our shop's chatbot! You can order food or inquire about Meal options.
    """)

    st.subheader("To chat with bot click Below!!")

    

    if 'stage' not in st.session_state:
        st.session_state.stage = 0

    def streamdata(i):
        st.session_state.stage = i

    def veg_menu():
        for item, img_url in veg_images.items():
            st.image(img_url, caption=item)

    def nonveg_menu():
        for item, img_url in nonveg_images.items():
            st.image(img_url, caption=item)

    def all_menu():
        for item, img_url in all_images.items():
            st.image(img_url, caption=item)

    def dessert_menu():
        for item, img_url in dessert_images.items():
            st.image(img_url, caption=item)

    if st.session_state.stage == 0:
        st.button('Mega-Bot', on_click=streamdata, args=[1])

    if st.session_state.stage >= 1:
        name = st.text_input('Name', key='name_input', value=st.session_state.get('name', ''), on_change=streamdata, args=[2])
        st.session_state.name = name

    pref = None
    if st.session_state.stage >= 2:
        st.write(f'Hello {st.session_state.name}!')
        pref = st.selectbox(
            'Pick your Preference',
            [None, 'Veg','Non Veg','Desserts','All'],
            on_change=streamdata, args=[3]
        )
        if pref is None:
            streamdata(2)

    if st.session_state.stage >= 3:
        st.write(f'Your preference is : {pref}')
        st.button('Start Over', on_click=streamdata, args=[0])
        st.button('Next', on_click=streamdata,args=[4])

    if st.session_state.stage >= 4:
        if pref.lower() == "veg":
            st.write(f"Would you prefer enjoying crunchy snacks or want to enjoy a {pref} Meal ?")
            veg_menu()
        elif pref.lower() == "nonveg" or pref.lower() == "non veg":
            st.write(f"Would you prefer enjoying crunchy snacks or want to enjoy a {pref} Meal ?")
            nonveg_menu()
        elif pref.lower() == "desserts":
            dessert_menu()
        elif pref.lower() == "all":
            st.write(f"Would you prefer enjoying crunchy snacks or want to enjoy a Meal ?")
            all_menu()
            st.text("Let me know if you have a personal preference:")
            if prompt := st.text_input("You:"):

                if st.button("Send"):
                    if prompt == "I want to ask you something different ":
                        st.text_area("Chatbot:", value="Sure, go ahead!", height=100, max_chars=None, key=None)
                    if prompt == "show options":
                        st.session_state.stage = 3
                    if prompt == "Do you know how to order?":
                        st.text_area("Chatbot:",value="Please contact owner at megaBite@gmail.com",height=100,max_chars=None,key=None)
                    if prompt == "Desserts":
                        st.session_state.stage = 3
                    else:
                        response = respond(prompt)
                        st.text_area("Chatbot:", value=response, height=100, max_chars=None, key=None)

# Run the Streamlit app
if __name__ == "__main__":
    main()
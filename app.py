
import pickle
import streamlit as st

pickle_in = open('modelmodel2.pkl', 'rb')

clf = pickle.load(pickle_in)


@st.cache()
@st.cache_data(show_spinner=False)

def make_prediction(bhk, Bathroom, Size, City):
    if City == 'Mumbai':
        city_enc = 5
    elif City == 'Chennai':
        city_enc = 1
    elif City == 'Bangalore':
        city_enc = 0
    elif City == 'Hyderabad':
        city_enc = 3
    elif City == 'Delhi':
        city_enc = 2
    elif City == 'Kolkata':
        city_enc = 4
    
    prediction = clf.predict([[bhk, Bathroom, Size, city_enc]])[0]
    return prediction


def main():
    #front end elements
    html_temp = """
    <div style = "background-color:green;padding:13px">
    <h1 style = "color:blue;text-align:center;"> House Prices Prediction by Ilesanmi </h1>
    </div>
    """

    #front end 
    #st.markdown("![](https://miro.medium.com/max/640/1*D6s2K1y7kjE14swcgITB1w.png)")
    # Display an image with adjustable size
    import streamlit as st
    from PIL import Image

    img = Image.open("how-much.jpg")
    #st.image(img, width=800, height = 300)
    st.image(img, use_column_width=True)

    #following lines create the visuals
    City = st.selectbox('City', ('Mumbai','Chennai','Bangalore','Hyderabad','Delhi','Kolkata'))    
    Bathroom = st.number_input('Enter number of Bathroom', step = 1)
    Size = st.number_input('Enter Size of the Land', step = 1)
    bhk = st.number_input('Enter number of BHK', step = 1)

    #when 'predict' is clicked, make prediction
    if st.button('Make Prediction'):
        result = make_prediction(bhk, Bathroom, Size, City)
        st.success('The price is mostlikely: {}'.format(result))
        #print('Just test')

if __name__ == '__main__':
    main()



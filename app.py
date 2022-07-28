import streamlit as st
import requests
from PIL import Image

image = Image.open('image.png')
image1 = Image.open('image1.png')
image2 = Image.open('image2.png')
image3 = Image.open('image3.png')
image4 = Image.open('image4.png')
image5 = Image.open('image5.png')
st.set_page_config(layout="wide")
st.title('Future Trend Analysis')
st.caption('Providing recommendations on basis of social media trends')
if st.button('Tshirts'):
    
    col1, col2= st.columns(2)
    with col1:
        st.subheader("Twitter")
        st.image(image,width=400)
    with col2:
        st.subheader("Flipkart")
        st.image(image1,width=400)
    url="http://flipkart.com/fastcolors-solid-men-round-neck-brown-t-shirt/p/itm206d93684e003?pid=TSHG4BM2SXFGQPPB&lid=LSTTSHG4BM2SXFGQPPBYCIS5T&marketplace=FLIPKART&store=clo%2Fash%2Fank%2Fedy&srno=b_3_86&otracker=browse&fm=organic&iid=09a0a7e6-7da8-487f-8f7b-107f233c6e8e.TSHG4BM2SXFGQPPB.SEARCH&ppt=None&ppn=None&ssid=qc4bqvncjk0000001658749324876"
    url1 = "http://flipkart.com/roden-striped-men-round-neck-yellow-t-shirt/p/itm3744da595cc60?pid=TSHFKAZFH6ETFP69&lid=LSTTSHFKAZFH6ETFP69UPZJQK&marketplace=FLIPKART&store=clo%2Fash%2Fank%2Fedy&srno=b_5_165&otracker=browse&fm=organic&iid=5f36eec8-b866-4818-acfd-fc96b59362fd.TSHFKAZFH6ETFP69.SEARCH&ppt=None&ppn=None&ssid=wi9d7ehkmo0000001658749327073"
    url2="http://flipkart.com/try-color-block-men-round-neck-maroon-beige-t-shirt/p/itm1e9001f0244a3?pid=TSHFGMGKGHE3SCTR&lid=LSTTSHFGMGKGHE3SCTRBE8PK1&marketplace=FLIPKART&store=clo%2Fash%2Fank%2Fedy&srno=b_10_374&otracker=browse&fm=organic&iid=1a3c65da-ab4a-4f52-bda8-58dd5a54d54b.TSHFGMGKGHE3SCTR.SEARCH&ppt=None&ppn=None&ssid=rb4s26l0yo0000001658749334580"
    url3="http://flipkart.com/helmont-color-block-men-hooded-neck-red-black-t-shirt/p/itmfdfvufw3fmuhz?pid=TSHFDFTFFR2QUDWV&lid=LSTTSHFDFTFFR2QUDWVQIYWB1&marketplace=FLIPKART&store=clo%2Fash%2Fank%2Fedy&srno=b_1_10&otracker=browse&fm=organic&iid=823eddf6-e251-4765-a614-ffa6ffd23e62.TSHFDFTFFR2QUDWV.SEARCH&ppt=None&ppn=None&ssid=gr7r5v2otc0000001658749322557"
    url4="http://flipkart.com/reya-striped-men-round-neck-blue-t-shirt/p/itm89a5018480b93?pid=TSHFURHKZYPSPGQR&lid=LSTTSHFURHKZYPSPGQRVEMJSX&marketplace=FLIPKART&store=clo%2Fash%2Fank%2Fedy&srno=b_1_35&otracker=browse&fm=organic&iid=823eddf6-e251-4765-a614-ffa6ffd23e62.TSHFURHKZYPSPGQR.SEARCH&ppt=None&ppn=None&ssid=gr7r5v2otc0000001658749322557"
    st.subheader("Shop Most trending items on flipkart")
    col3, col4, col5, col6, col7= st.columns(5)
    with col3:
        st.markdown("[item1](%s)" % url)
    with col4:    
        st.markdown("[item2](%s)" % url1)
    with col5:
        st.markdown("[item3](%s)" % url2)
    with col6:
        st.markdown("[item4](%s)" % url3)
    with col7:
        st.markdown("[item5](%s)" % url4)
        
if st.button('Skirts'):
    col1, col2= st.columns(2)
    with col1:
        st.subheader("Twitter")
        st.image(image2,width=400)
    with col2:
        st.subheader("Flipkart")
        st.image(image3,width=400)
    url5="http://flipkart.com/montrez-solid-women-straight-dark-blue-skirt/p/itm918546888c1f2?pid=SKIGFHMYPMAR6DYH&lid=LSTSKIGFHMYPMAR6DYHPXXFVJ&marketplace=FLIPKART&store=clo%2Fvua%2Fiku%2Fw5t&srno=b_1_7&otracker=browse&fm=organic&iid=2d939601-ec13-4558-93c7-7dbe65e7c6c7.SKIGFHMYPMAR6DYH.SEARCH&ppt=None&ppn=None&ssid=il2xkxlcsg0000001658754628910"
    url6 = "http://flipkart.com/krishika-printed-women-flared-maroon-skirt/p/itmfda3283270e43?pid=SKIFT57NCPGY8WZC&lid=LSTSKIFT57NCPGY8WZCUFRSSN&marketplace=FLIPKART&store=clo%2Fvua%2Fiku%2Fw5t&srno=b_4_150&otracker=browse&fm=organic&iid=c2e8f37a-c917-4619-a1ec-36a3b794b8a7.SKIFT57NCPGY8WZC.SEARCH&ppt=None&ppn=None&ssid=7rw6oula680000001658754631703"
    url7="http://flipkart.com/dl-fashion-solid-women-pleated-black-skirt/p/itm845f404d52860?pid=SKIFVJ3VFYAF2FWF&lid=LSTSKIFVJ3VFYAF2FWFR5XU8G&marketplace=FLIPKART&store=clo%2Fvua%2Fiku%2Fw5t&srno=b_8_317&otracker=browse&fm=organic&iid=23d51186-d045-46b1-81f9-198d2c6b7bee.SKIFVJ3VFYAF2FWF.SEARCH&ppt=None&ppn=None&ssid=okephamwgw0000001658754635720"
    url8="https://www.flipkart.com/fashioncutz-printed-women-flared-pink-skirt/p/itm701c3ae7da4c5?pid=SKIFUKMJFBPFYZRZ&lid=LSTSKIFUKMJFBPFYZRZRPYZJX&marketplace=FLIPKART&store=clo%2Fvua%2Fiku%2Fw5t&srno=b_9_355&otracker=browse&fm=organic&iid=69e239c2-1a67-45ba-9cb3-ef8a7f54c146.SKIFUKMJFBPFYZRZ.SEARCH&ppt=None&ppn=None&ssid=mby6gqd8740000001658754636747"
    url9="http://flipkart.com/uptownie-lite-solid-women-pleated-green-skirt/p/itmcaaf54207db18?pid=SKIFZRZ4XJ5YPW57&lid=LSTSKIFZRZ4XJ5YPW57UOYO5K&marketplace=FLIPKART&store=clo%2Fvua%2Fiku%2Fw5t&srno=b_1_27&otracker=browse&fm=organic&iid=en_tlm01bTVb0MQukMn17A1DGU2ACxrVAO4PHGxxoirmPZgfUjIy6bB2BRPWME5eodiNRmifKLg5oSKJG5Jr58DRg%3D%3D&ppt=None&ppn=None&ssid=il2xkxlcsg0000001658754628910"
    st.subheader("Shop Most trending items on flipkart")
    col3, col4, col5, col6, col7= st.columns(5)
    with col3:
        st.markdown("[item1](%s)" % url5)
    with col4:    
        st.markdown("[item2](%s)" % url6)
    with col5:
        st.markdown("[item3](%s)" % url7)
    with col6:
        st.markdown("[item4](%s)" % url8)
    with col7:
        st.markdown("[item5](%s)" % url9)
if st.button('Dresses'):
    col1, col2= st.columns(2)
    with col1:
        st.subheader("Twitter")
        st.image(image4,width=400)
    with col2:
        st.subheader("Flipkart")
        st.image(image5,width=400)
    url10="http://flipkart.com/daevish-women-skater-black-dress/p/itme6983dab1e838?pid=DREFXCHTHDP7FG3C&lid=LSTDREFXCHTHDP7FG3CYGLEXF&marketplace=FLIPKART&store=clo%2Fodx%2Fmaj%2Fjhy&srno=b_1_16&otracker=browse&fm=organic&iid=9f4db607-5fab-4c8e-8f54-49bcaf7d2f85.DREFXCHTHDP7FG3C.SEARCH&ppt=None&ppn=None&ssid=935ax4ah8g0000001658756734118"
    url11 = "http://flipkart.com/aayu-women-fit-flare-multicolor-dress/p/itmfbz6zajmnsthr?pid=DREFBYMF96XFYZBJ&lid=LSTDREFBYMF96XFYZBJUGRSL8&marketplace=FLIPKART&store=clo%2Fodx%2Fmaj%2Fjhy&srno=b_1_3&otracker=browse&fm=organic&iid=9f4db607-5fab-4c8e-8f54-49bcaf7d2f85.DREFBYMF96XFYZBJ.SEARCH&ppt=None&ppn=None&ssid=935ax4ah8g0000001658756734118"
    url12="http://flipkart.com/sheetal-associates-women-bodycon-blue-dress/p/itm2bd5351d35b2c?pid=DREG49M2XKYBVDMF&lid=LSTDREG49M2XKYBVDMFT8XKLL&marketplace=FLIPKART&store=clo%2Fodx%2Fmaj%2Fjhy&srno=b_3_89&otracker=browse&fm=organic&iid=518e877b-2c85-48a1-b683-3dc7f39eb17a.DREG49M2XKYBVDMF.SEARCH&ppt=None&ppn=None&ssid=3253kt4y000000001658756736902"
    url13="http://flipkart.com/kannan-women-maxi-multicolor-dress/p/itmffz9mr7zsftg4?pid=DREFFWUHMJYGMUSC&lid=LSTDREFFWUHMJYGMUSCT5DLSN&marketplace=FLIPKART&store=clo%2Fodx%2Fmaj%2Fjhy&srno=b_5_190&otracker=browse&fm=organic&iid=9db22210-7319-4f31-8a7d-13cb2f0edf9f.DREFFWUHMJYGMUSC.SEARCH&ppt=None&ppn=None&ssid=vtbp9w2e2o0000001658756739007"
    url14="http://flipkart.com/sheetal-associates-women-maxi-pink-dress/p/itm3f423fd6c7ca2?pid=DREGCBJHUCSTJBBS&lid=LSTDREGCBJHUCSTJBBSVHZTOX&marketplace=FLIPKART&store=clo%2Fodx%2Fmaj%2Fjhy&srno=b_1_20&otracker=browse&fm=organic&iid=9f4db607-5fab-4c8e-8f54-49bcaf7d2f85.DREGCBJHUCSTJBBS.SEARCH&ppt=None&ppn=None&ssid=935ax4ah8g0000001658756734118"
    st.subheader("Shop Most trending items on flipkart")
    col3, col4, col5, col6, col7= st.columns(5)
    with col3:
        st.markdown("[item1](%s)" % url10)
    with col4:    
        st.markdown("[item2](%s)" % url11)
    with col5:
        st.markdown("[item3](%s)" % url12)
    with col6:
        st.markdown("[item4](%s)" % url13)
    with col7:
        st.markdown("[item5](%s)" % url14)
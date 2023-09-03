import streamlit as st

st.markdown ("# Blog")
txt = ('this is my blog area where i will present the different blogs and links to read')
st.info(txt)
col1, col2, col3 = st.columns(3)

url = "https://www.linkedin.com/pulse/what-etl-advantages-using-professionally-imanol-asolo/?trackingId=Kna1OS3TTdyZ0%2F9vq6oO6A%3D%3D"
col1.success("[What is an ETL and advantages for using it profesionally](%s)" %url)
url1 = "https://www.linkedin.com/pulse/full-stack-graphql-comprehensive-guide-imanol-asolo/?trackingId=xt6TjhChR%2B6Dcy61Zzz1Pw%3D%3D"
col1.success('[Full Stack GraphQL: A Comprehensive Guide](%s)' %url1)
url3 = "https://www.linkedin.com/pulse/hire-full-stack-developer-scrum-master-skills-whole-universe-asolo/?trackingId=ePrutKwySbmX%2FLPlr2lPLA%3D%3D"
col1.success('[Hire a Full Stack Developer with Scrum Master skills, the whole IT universe in your hands!](%s)' %url3)
url4 = "https://www.linkedin.com/pulse/full-stack-developer-scrum-master-imanol-asolo/?trackingId=3ov%2FSchKQpSFJmb03z01wA%3D%3D"
col2.warning('[Full Stack Developer + Scrum Master](%s)' %url4)
url5 = "https://www.linkedin.com/newsletters/codecodix-road-nomad-notebook-7001205963869290496/"
col2.warning('[Generalist vs Specialist in IT Industry](%s)'%url5)
url6= "https://www.linkedin.com/pulse/metodolog%25C3%25ADa-agile-trabaja-en-equipo-para-conseguir-tus-imanol-asolo/?trackingId=tzjIjVIbQr6iZgmrlItx%2FQ%3D%3D"
col2.warning('[Metodología Agile, trabaja en equipo para conseguir tus objetivos.](%s)'%url6)
url7="https://www.linkedin.com/pulse/agile-methodologies-development-mid-large-sized-food-processing/?trackingId=fz6qUm58R4Korx1c8xtx%2Bg%3D%3D"
col3.error('[Agile methodologies development in mid and large sized food processing companies](%s)'%url7)
url8="https://www.linkedin.com/pulse/scrum-master-multiverse-imanol-asolo/?trackingId=wUdPONOxSlm2tEe2%2BUr19w%3D%3D"
col3.error('[A Scrum Master in the Multiverse](%s)'%url8)
url9="https://www.linkedin.com/pulse/pros-cons-using-erp-software-your-company-imanol-asolo/?trackingId=4Ktl%2FADCSeCOjTUiGjrPnw%3D%3D"
col3.error('[Pros and Cons about using an ERP software in your company.](%s)'%url9)
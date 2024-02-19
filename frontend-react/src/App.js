import React, { useState, useEffect } from 'react'

function App() {

  const [newsData, setNewsData] = useState([{}])


  useEffect(() => {
    fetch("/news").then(
      res => res.json()
    ).then(
      data => {
        setNewsData(data)
        console.log(data)
      }
    )
  }, [])

  const formattedDate = (date) => {
    date = new Date(date)
    return `${date.getDate()}-${date.getMonth() + 1}-${date.getFullYear()}`
  }

    return(
      <>
      {newsData.length === 0 ? (
      <p>Loading...</p>
    ) : (
      newsData.map((newsItem, i) => (
        <div key={i}>
          <h2>{newsItem.title}</h2>
          <p>{formattedDate(newsItem.publishedAt)}</p>
          <p>{newsItem.description}</p>
          <a href={newsItem.url}>Read more</a>
        </div>
      ))
    )}
      </>
    )
}


export default App;

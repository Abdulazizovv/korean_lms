import { BrowserRouter, Routes, Route } from 'react-router-dom'
import IndexPage from './pages/IndexPage'
import Navbar from './components/Navbar'
import '@fontsource/roboto/300.css';

function App() {

  return (
    <>
      <BrowserRouter>
      <Navbar />
        <Routes>
          <Route path="/" element={<IndexPage/>} />
        </Routes>
      </BrowserRouter>
    </>
  )
}

export default App

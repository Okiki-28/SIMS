import { Button } from "../components/Button";
import React, { useMemo, useState } from "react";
import { Modal } from "../components/Modal";
import { useSelector } from "react-redux";
import api from "../api/client";
import { useNavigate } from "react-router-dom"
import { Link } from "react-router-dom";



export const Navbar = () => {

    const navigate = useNavigate()

    const [isLoading, setIsLoading] = useState(false)
    const [error, setError] = useState("")

    const company_reg_no = useMemo(() => {
        const savedUser = localStorage.getItem("user");
        return savedUser ? JSON.parse(savedUser).company_reg_no : "";
    }, []);
    const user_id = useMemo(() => {
        const savedUser = localStorage.getItem("user");
        return savedUser ? JSON.parse(savedUser).user_id : "";
    }, []);
    const user = useMemo(() => {
        const savedUser = localStorage.getItem("user");
        return savedUser ? JSON.parse(savedUser).username : "";
    }, []);
    let pageHeading = useSelector((state: any) => state.heading.value.heading)
    let message = useSelector((state: any) => state.heading.value.message)
    const closeModal = () => {
        setIsActive(false)
    }

    const [isActive, setIsActive] = useState(false)
    const [modalHeading, setModalHeading] = useState("")
    const [modalData, setModalData] = useState({})
    const [isModalForm, setIsModalForm] = useState(false)
    const addProduct = () => {
        setModalHeading("Add")
        const data = {
            "name": "",
            "description": "",
            "quantity": 0,
            "price": 0,
            "selling_price": 0,
            "reorder_level": 0,
            "supplier": -1,
            "category": -1
        }
        setModalData(data)
        setIsModalForm(true)
        setIsActive(true);
    }

    const handleAddProduct = async (e: React.FormEvent, formData: any) => {
        
        setError("")
        setIsLoading(true)
        console.log(formData)
        try {
            console.log(formData)
            const response = await api.post("/api/products/add", formData, { withCredentials: true });

            return response.data
        } catch (err:any) {
            if (err?.response) {
                setError(err.response.data.details)
            } else {
                setError("Unable to add product")
            }
            return {"error": err.response.data.details}
        }
        
    }

    const logout = () => {
        
        navigate("/Logout")
    }

    return (
        <>
        <Modal heading={modalHeading} isActive={isActive} isModalForm={isModalForm} data={modalData} handleSubmit={handleAddProduct} onClose={closeModal}  />
        <section className="top-bar">
            <h1>Company Name</h1>
            <section className="nav-bar">
                <ul>
                    <li className={pageHeading == "Dashboard"? "active": ""}><Link to="/dashboard">Dashboard</Link></li>
                    <li className={pageHeading == "Inventory"? "active": ""}><Link to="/inventory">Inventory</Link></li>
                    <li className={pageHeading == "Counter Sale"? "active": ""}><Link to="/counter-sale">Counter Sale</Link></li>
                    <li className={pageHeading == "Reports"? "active": ""}><Link to="/reports">Reports</Link></li>
                    <li className={pageHeading == "Settings"? "active": ""}><Link to="/settings">Settings</Link></li>
                </ul>
            </section>
            <div className="functionality">
                <Button onclick={addProduct}>Add Products +</Button>
                <Button onclick={logout}>Logout</Button>
            </div>
        </section>
        </>
    )
};
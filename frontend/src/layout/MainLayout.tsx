import React from "react";
import { Navbar } from "./Navbar";
import { Sidebar } from "./Sidebar";

import { useMemo, useState } from "react";
import { Modal } from "../components/Modal";
import { useSelector } from "react-redux";

type Props = {
    children: React.ReactNode;
};

export default function MainLayout({ children }: Props) {
    const user = useMemo(() => {
            const savedUser = localStorage.getItem("user");
            return savedUser ? JSON.parse(savedUser).username : "";
    }, []);
    let pageHeading = useSelector((state: any) => state.heading.value.heading)
    let message = useSelector((state: any) => state.heading.value.message)

    return (
        <main className="main-layout">
            <Navbar />
            <div className="page-heading">
                <h1>{pageHeading}</h1>
                <p>Welcome {user}, {message}</p> 
            </div>
            <main className="content">{children}</main>
            {/* <Sidebar /> */}
        </main>
    )
} 
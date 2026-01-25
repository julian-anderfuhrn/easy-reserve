export default function Footer() {
    const year = new Date().getFullYear();

    return (
        <footer className="bg-gray-200 text-center p-4 text-sm">
            © {year} EasyReserve
        </footer>
    );
}


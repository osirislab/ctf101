# Recommended Software

Generally in cyber security competitions, it is up to you and your team
to determine what software to use. In some cases you may even end up
creating new tools to give you an edge! That being said, here are some
applications that we recommend for most competitors for most
competitions.

## Disassemblers/Decompilers

-   [Ghidra](https://ghidra-sre.org/)

    Ghidra is a disassembler and decompiler that is open source and free
    to use. Released by the NSA, Ghidra is a capable tool and is the
    recommended disassembler for most use cases. An alternative is IDA
    Pro (a cyber security industry standard), however IDA Pro is not
    free and licenses are very expensive.

-   [Binary Ninja](https://binary.ninja/)

    Binary Ninja is a commercial disassembler (with a free demo
    application) that provides an aesthetic and easy to use interface
    for binary reverse engineering. It also has a Web-UI which can be
    used freely. Binary Ninja's API and intermediate language make it
    superior than other disassemblers for certain use cases.

## Debuggers

-   [Pwndbg for GDB](https://github.com/pwndbg/pwndbg/)

    Pwndbg is a plugin for the GNU Debugger (gdb) which makes it easier
    to dynamically reverse an application by stepping through its
    execution. In order to use pwndbg you will first need to have gdb
    installed via a Linux virtual machine or similar.

-   [WinDbg](https://docs.microsoft.com/en-us/windows-hardware/drivers/debugger/)

    WinDbg is a debugger for Windows applications.

## Web Tools

-   [Burp Suite](https://portswigger.net/burp/communitydownload/)

    Burp Suite is an HTTP proxy and set of tools which allow you to
    view, edit and replay your HTTP requests. While Burp Suite is a
    commercial tool, it offers a free version which is very capable and
    usually all that's needed.

-   [sqlmap](http://sqlmap.org/)

    sqlmap is a penetration testing tool that automates hte process of
    detecting and exploiting SQL injection flaws. It's open source and
    freely available.

-   [Google Chrome](https://www.google.com/chrome/)

    Google Chrome is a web browser with a suite of developer tools and
    extensions. These tools and extensions can be useful when
    investigating a web application.

-   [Wireshark](https://www.wireshark.org/download.html/)

    Wireshark is a PCAP analysis tool which allows you to analyze and
    record network traffic.

## Virtualization

-   [VMware](https://www.vmware.com/products/personal-desktop-virtualization.html/)

    VMware is a company that creates virtualization software that allows
    you to run other operating systems within your existing operating
    system. While their products are not generally free, their software
    is best in class for virtualization.

    VMWare Fusion, VMWare Workstation, and VMWare Player are three of
    their virtualization products that can be used on your computer to
    run other OS'es. [VMWare
    Player](http://www.vmware.com/go/downloadplayer/) is free to use for
    Windows and Linux.

-   [VirtualBox](https://www.virtualbox.org/)

    VirtualBox is open source virtualization software which allows you
    to virtualize other operating systems. It's very similar to VMWare
    products but free for all OS'es. It is generally slower than VMWare
    but works well enough for most people.

## Programming

-   [Python](https://www.python.org/downloads/)

    Python is an easy-to-learn, widely used programming language which
    supports complex applications as well as small scripts. It has a
    large community which provides thousands of useful packages. Python
    is widely used in the cyber security industry and is generally the
    recommended language to use in CTF competition.

-   [pwntools](http://docs.pwntools.com/en/stable/install.html)

    Pwntools is a Python package which makes interacting with processes
    and networks easy. It is a recommended library for interacting with
    binary exploitation and networking based CTF challenges.

    !!!note
        You can run
        [pwntools](http://docs.pwntools.com/en/stable/install.html) right in
        your browser by using [repl.it](https://repl.it/). Create a new
        Python repl and install the `pwntools` package. After that you'll
        be able to use pwntools directly from your browser without having to
        install anything.

## Miscellaneous

-   [CyberChef](https://gchq.github.io/CyberChef/)

    CyberChef is a simple web app for analysing and decoding data
    without having to deal with complex tools or programming languages.
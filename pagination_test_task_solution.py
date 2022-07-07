import argparse


def argument_validator(func_name):
    def validate_args(total_pages, current_page, around, boundaries):
        values = [total_pages, current_page, around, boundaries]
        for value in values:
            if type(value) is not int:
                raise TypeError(f'Values must be integers.')
            elif value < 0:
                raise ValueError("Values should not be negative.")

        if total_pages == 0 or current_page == 0:
            raise ValueError("Current and Total Page must be larger than 0.")

        if current_page > total_pages:
            raise ValueError(f"current_page '{current_page}' can" +
                             f" not be larger than total_pages '{total_pages}'")

        return func_name(total_pages, current_page, around, boundaries)
    return validate_args


@argument_validator
def get_footer_pagination(total_pages, current_page, around, boundaries):
    # Create three different lists for start, middle and end
    if boundaries == 0:
        pages_from_start = []
        pages_from_end = []
    else:
        pages_from_start = [*range(1, boundaries + 1)]
        pages_from_end = [*range(total_pages - boundaries + 1, total_pages + 1)]

    lower_end_around = 1 if current_page - around <= 1 else current_page - around
    higher_end_around = total_pages + 1 if (current_page + around + 1 >
                                            total_pages) else current_page + around + 1
    current_and_around = [
        *range(lower_end_around, higher_end_around)
    ]

    # Add pages from start list which are larger than current_page + around to
    # current_and_around
    for page in pages_from_start:
        if page > current_and_around[-1] and page <= total_pages:
            current_and_around.append(page)

    # Add pages from end list which are smaller than current_page - around to
    # current_and_around
    for page in pages_from_end:
        if page < current_and_around[0] and page >= 1:
            current_and_around.insert(0, page)

    # Remove all duplicate pages from the three lists with list comprehension
    pages_from_start = [x for x in pages_from_start if x < current_page]

    pages_from_end = [x for x in pages_from_end if x > current_page]

    if pages_from_start and pages_from_end:
        current_and_around = [
            x for x
            in current_and_around
            if x > pages_from_start[-1] and x < pages_from_end[0]
        ]
    elif pages_from_start and not pages_from_end:
        current_and_around = [
            x for x
            in current_and_around
            if x > pages_from_start[-1] and x <= total_pages
        ]
    elif not pages_from_start and pages_from_end:
        current_and_around = [
            x for x
            in current_and_around
            if x >= 1 and x < pages_from_end[0]
        ]
    else:
        current_and_around = [
            x for x
            in current_and_around
            if x >= 1 and x <= total_pages
        ]

    # Insert '...' where necessary
    if not pages_from_start and current_and_around[0] > 2:
        current_and_around.insert(0, '...')
    elif pages_from_start and current_and_around[0] > pages_from_start[-1] + 1:
        current_and_around.insert(0, '...')

    if not pages_from_end and current_and_around[-1] < total_pages - 1:
        current_and_around.append('...')
    elif not pages_from_end and boundaries == 0 and current_and_around[-1] < total_pages:
        current_and_around.append('...')
    elif pages_from_end and current_and_around[-1] < pages_from_end[0] - 1:
        current_and_around.append('...')

    pages = pages_from_start + current_and_around + pages_from_end
    return pages


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--current_page", help="Current Page Number", required=True, type=int)
    parser.add_argument("--total_pages", help="Total Page Number", required=True, type=int)
    parser.add_argument("--boundaries", help="Boundaries Number", required=True, type=int)
    parser.add_argument("--around", help="Around Number", required=True, type=int)

    args = parser.parse_args()

    total_pages = args.total_pages
    current_page = args.current_page
    around = args.around
    boundaries = args.boundaries

    print(*get_footer_pagination(total_pages=total_pages, current_page=current_page,
                                 around=around, boundaries=boundaries))
